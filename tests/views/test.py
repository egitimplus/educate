import math
from django.db import transaction
from django.http import HttpResponseServerError
from rest_framework import viewsets, mixins, status
from tests.models import Test, TestUnique
from tests.serializers import TestSerializer, TestPostSerializer, SimpleTestSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from educategories.serializers import EduCategorySimpleSerializer
from questions.serializers import QuestionSerializer
from questions.models import QuestionAnswerStat, QuestionUnique, QuestionUniqueStat
from components.models import ComponentAnswerStat, ComponentStat, ComponentAnswer
from questions.feeds import QuestionRepository
from components.feeds import ComponentStatRepository, ComponentsStatRepository, ComponentRepository
from tests.feeds import TestRepository
import itertools


class TestViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return TestPostSerializer

        return TestSerializer

    @action(methods=['GET'], detail=True)
    def view(self, request, pk=None):
        queryset = Test.objects.prefetch_related('questions','categories').filter(id=pk).first()

        questions = QuestionSerializer(queryset.questions.order_by('question').all(), many=True)
        categories = EduCategorySimpleSerializer(queryset.categories.all(), many=True)

        response = {
            'id': queryset.id,
            'name': queryset.name,
            'test_seconds': queryset.test_seconds,
            'active': queryset.active,
            'questions': questions.data,
            'categories': categories.data
        }
        return Response(response)

    @action(methods=['POST'], detail=False)
    def search(self, request):
        # TODO publisher yetkisi var mı bakılmalı
        publisher = request.data.get('publisher_id', None)
        search_text = request.data.get('search_text', None)

        if not publisher:
            return Response('Yayınevi bulunamadı.', status=status.HTTP_400_BAD_REQUEST)

        queryset = Test.objects.filter(publisher_id=publisher)

        if search_text:
            queryset = queryset.filter(name__icontains=search_text)

        serializer = SimpleTestSerializer(queryset, many=True)

        return Response(serializer.data)

    '''
    # react 
    # -----------------------------------------------------------------------------------------------------------------
    # list()            : kurs listesi
    # finish()          : 
    '''

    '''
    ' Yapılacak Güncelleme İşlemleri
    '------------------------------------------------------------------------------------------------
    ' TestUnique            : Benzersiz test bilgisi eklenecek ve güncellenecek - test_unique
    ' QuestionUnique        : Benzersiz soru durum güncellemesi yapılacak - question_unique
    ' QuestionUniqueStat    : Benzersiz soru istatistikleri eklenecek - question_unique_stat
    ' QuestionAnswerStat    : Soru cevap istatistikleri eklenecek - question_answer_stat 
    ' ComponentAnswerStat   : Soru parçası istatistikleri eklenecek - component_answer_stat
    ' -ComponentStat         : Soru parçası durum güncellemesi yapılacak - component_stat
    ' -ComponentStatusChange : Cron job ile güncellenecek soru parçaları - component_status_change
    '------------------------------------------------------------------------------------------------
    '''
    @transaction.atomic
    @action(methods=['POST'], detail=False)
    def finish(self, request):

        answers = request.data.get('answers', None)
        test_id = request.data.get('test_id', None)

        if len(answers) < 1:
            return HttpResponseServerError("You must answer a question.")

        queryset = Test.objects.prefetch_related(
            'questions',
            'questions__component',
            'questions__answers',
            'questions__answers__answer_components'
        ).get(id=test_id)

        test = TestRepository(request=request, test=queryset)

        test_answer = test.answer()
        test_unique = test_answer.test_unique

        questions = test.questions()

        test_answer.total_question = len(questions)

        for question in questions:
            qr = QuestionRepository(request=request, question=question)

            i = 0
            answer_is_true = 0

            # post edilen soru cevaplarına göre veri tabanında gerekli düzenlemeleri yapalım
            for answer in answers:
                # Eğer post edilen cevaplar içerisinde bu soru için cevap bulunduysa
                if answer['question_id'] == question.id:
                    question_answer_id = answer['answer_id']
                    i = i + 1
                    # Eğer post edilen cevap doğru ise
                    if question_answer_id == qr.true_answer.id:
                        true_components = qr.add_true_answer(test_unique=test_unique)
                        test_answer.true_components.append(true_components)
                        test_answer.true_question = test_answer.true_question + 1
                        # cevabı soru istatistiklerine ekleyelim
                        qr.add_question_answer(
                            test_unique=test_unique,
                            question_answer_id=question_answer_id,
                            answer_is_true=1
                        )
                        answer_is_true = 1
                    # Eğer post edilen cevap yanlış ise
                    else:
                        component_answers = ComponentAnswer.objects.select_related(
                            'component'
                        ).filter(question_answer_id=question_answer_id).all()

                        if len(component_answers) > 0:
                            # sorudaki soru parçaları için gerekli işlemleri yapalım
                            for component_answer in component_answers:
                                csr = ComponentStatRepository(request=self.request, component=component_answer.component)
                                if component_answer.component_ok == 1:
                                    # soru parçasını doğru soru parçası listesine ekleyelim
                                    true_components = csr.add_true_answer(question=question, test_unique=test_unique)
                                    test_answer.true_components.append(true_components)
                                else:
                                    # soru parçasını yanlış soru parçası listesine ekleyelim
                                    false_components = csr.add_false_answer(question=question, test_unique=test_unique)
                                    test_answer.false_components.append(false_components)
                        else:
                            # soru parçasını yanlış soru parçası listesine ekleyelim
                            false_components = qr.add_false_answer(test_unique=test_unique)
                            test_answer.false_components.append(false_components)

                        test_answer.false_question = test_answer.false_question + 1
                        # cevabı soru istatistiklerine ekleyelim
                        qr.add_question_answer(
                            test_unique=test_unique,
                            question_answer_id=question_answer_id,
                            answer_is_true=0
                        )

            # Eğer post edilen cevaplar içerisinde bu soru için cevap bulunamadıysa
            if i == 0:
                # soru parçasını boş soru parçası listesine ekleyelim
                empty_components = qr.add_empty_answer(test_unique=test_unique)
                test_answer.empty_components.append(empty_components)

                # boş soru sayısını bir artıralım
                test_answer.empty_question = test_answer.empty_question + 1

            # question unique oluşturularım ve istatistikleri ekleyelim
            qr.create_question_unique(answer_is_true)

        # sorulardaki soru parçalarını birleştirelim ve tekleştirelim.
        all_components = test_answer.all_components()

        # veritabanından tekleştirilen soru parçalarına ait durum bilgilerini çekelim
        component_stats = ComponentStat.objects.filter(
            component_id__in=all_components,
            user=request.user
        ).values('id', 'component_id', 'component_status')

        component_stat_repo = ComponentsStatRepository(
            request=request,
            component_stats=component_stats,
            answers=test_answer
        )

        for component in all_components:
            component_stat_repo.update_component_status(component)

        test_result = test_answer.test_result()

        TestUnique.objects.filter(ids=test_unique.id).update(test_result=test_result)

        return Response([])
