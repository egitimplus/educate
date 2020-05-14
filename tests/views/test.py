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
from components.feeds import ComponentStatRepository, ComponentIdRepository
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

        question_repo = QuestionRepository(request=request)
        component_id_repo = ComponentIdRepository(request=request)

        queryset = Test.objects.prefetch_related(
            'questions',
            'questions__component',
            'questions__answers',
            'questions__answers__answer_components'
        ).get(id=test_id)

        test_unique = TestUnique.objects.create(
            user_id=request.user.id,
            test_id=queryset.id,
            report='report',
            test_result=0
        )

        questions = queryset.questions.order_by('question').all()

        result = {
            'total_questions': len(questions),
            'true_questions': 0,
            'false_questions': 0,
            'empty_questions': 0
        }

        components = {
            'all': [],
            'true': [],
            'false': [],
            'empty': []
        }

        for question in questions:
            # soruya ait soru parçalarını veritabanından çekelim
            question_components = question.component.all().values_list('id', flat=True)

            # soruya ait soru parçalarını listeye ekleyelim ve küçükten büyüğe göre sıralayalım
            question_components_unique = list(question_components)
            question_components_unique.sort()

            # tüm sorulara ait soru parçalarını listeye ekleyelim
            components['all'].append(question_components_unique)

            # doğru soru cevabını çekelim ve soru tiplerinden unique bir kod oluşturalım
            # benzer soruları bu şekilde tespit edeceğiz
            question_answer = question.answers.filter(is_true_answer=1).first()
            question_code = '-'.join(map(str, question_components_unique))

            i = 0
            # post edilen soru cevaplarına göre veri tabanında gerekli düzenlemeleri yapalım
            for answer in answers:
                # Eğer post edilen cevaplar içerisinde bu soru için cevap bulunduysa
                if answer['question_id'] == question.id:

                    i = i + 1
                    # Eğer post edilen cevap doğru ise
                    if answer['answer_id'] == question_answer.id:
                        # sorudaki soru parçaları için gerekli işlemleri yapalım
                        for question_component in question_components:
                            # soru parçasını doğru soru parçası listesine ekleyelim
                            components['true'].append(question_component)

                            # cevabı soru parçası istatistiklerine ekleyelim
                            ComponentAnswerStat.objects.create(
                                component_id=question_component,
                                question_id=question.id,
                                test_unique_id=test_unique.id,
                                user_id=request.user.id,
                                answer_is_true=1,
                                answer_is_empty=0
                            )

                            # doğru soru sayısını bir artıralım
                            result['true_questions'] = result['true_questions'] + 1
                            answer_is_true = 1

                    # Eğer post edilen cevap yanlış ise
                    else:
                        component_answers = ComponentAnswer.objects.filter(question_answer_id=question_answer.id).all()
                        if len(component_answers) > 0:
                            # sorudaki soru parçaları için gerekli işlemleri yapalım
                            for component_answer in component_answers:
                                if component_answer.component_ok == 1:
                                    # soru parçasını doğru soru parçası listesine ekleyelim
                                    components['true'].append(component_answer.component_id)
                                    component_is_true = 1
                                else:
                                    # soru parçasını yanlış soru parçası listesine ekleyelim
                                    components['false'].append(component_answer.component_id)
                                    component_is_true = 0

                                # cevabı soru parçası istatistiklerine ekleyelim
                                ComponentAnswerStat.objects.create(
                                    component_id=component_answer.component_id,
                                    question_id=question.id,
                                    test_unique_id=test_unique.id,
                                    user_id=request.user.id,
                                    answer_is_true=component_is_true,
                                    answer_is_empty=0
                                )
                        else:
                            # sorudaki soru parçaları için gerekli işlemleri yapalım
                            for question_component in question_components:
                                # soru parçasını yanlış soru parçası listesine ekleyelim
                                components['false'].append(question_component)

                                # cevabı soru parçası istatistiklerine ekleyelim
                                ComponentAnswerStat.objects.create(
                                    component_id=question_component,
                                    question_id=question.id,
                                    test_unique_id=test_unique.id,
                                    user_id=request.user.id,
                                    answer_is_true=0,
                                    answer_is_empty=0
                                )

                        # yanlış soru sayısını bir artıralım
                        result['false_questions'] = result['false_questions'] + 1
                        answer_is_true = 0

                        # cevabı soru istatistiklerine ekleyelim
                        QuestionAnswerStat.objects.create(
                            answer_is_true=answer_is_true,
                            answer_seconds=0,
                            answer_type=1,
                            question_id=question.id,
                            user_id=request.user.id,
                            test_unique_id=test_unique.id,
                            question_answer_id=question_answer.id,
                            answer_count=1
                        )

            # soru unique kodunu veritabanında varsa güncelleyelim eğer yoksa ekleyelim
            obj, created = QuestionUnique.objects.get_or_create(
                question_code=question_code,
            )

            question_unique_stat = QuestionUniqueStat.objects.get(question_code=question_code)
            # verilen cevaba göre soru için yeni bir kod oluşturalım
            question_unique = question_repo.question_unique_status(question_unique_stat, answer_is_true)

            # unique soru istatistiklerini ekleyelim
            QuestionUniqueStat.objects.update_or_create(
                question_unique_id=obj.id,
                user_id=request.user.id,
                question_code=question_code,
                defaults={
                    "status": question_unique['status'],
                    "percent": question_unique['percent'],
                    "solved": question_unique['solved']
                }
            )

            # Eğer post edilen cevaplar içerisinde bu soru için cevap bulunamadıysa
            if i == 0:
                # boş soru sayısını bir artıralım
                result['empty_questions'] = result['empty_questions'] + 1
                # sorudaki soru parçaları için gerekli işlemleri yapalım
                for question_component in question_components:
                    # soru parçasını boş soru parçası listesine ekleyelim
                    components['empty'].append(question_component)

                    # cevabı soru parçası istatistiklerine ekleyelim
                    ComponentAnswerStat.objects.create(
                        component_id=question_component,
                        question_id=question.id,
                        test_unique_id=test_unique.id,
                        user_id=request.user.id,
                        answer_is_true=0,
                        answer_is_empty=1
                    )

        true_sub_components = component_id_repo.all_sub_components(components['true'])

        components['true'] = components['true'] + true_sub_components
        components['all'] = components['all'] + true_sub_components

        # sorulardaki soru parçalarını tekleştirelim.
        all_components = list(set(itertools.chain(*components['all'])))

        # veritabanından tekleştirilen soru parçalarına ait durum bilgilerini çekelim
        component_stats = ComponentStat.objects.filter(
            component_id__in=all_components,
            user=request.user
        ).values('id', 'component_id', 'component_status')

        component_stat_repo = ComponentStatRepository(
            request=request,
            component_stats=component_stats,
            components=components
        )

        for component in all_components:
            component_stat_repo.update_component_status(component)

        test_result = math.ceil((result['true_questions'] / result['total_questions']) * 100)

        if test_result > 100:
            test_result = 100

        TestUnique.objects.filter(ids=test_unique.id).update(test_result=test_result)

        return Response([])
