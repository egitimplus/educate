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
from tests.feeds import TestRepository


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
        queryset = Test.objects.prefetch_related('questions', 'categories').filter(id=pk).first()

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
    ' ComponentStat         : Soru parçası durum güncellemesi yapılacak - component_stat
    ' ComponentStatusChange : Cron job ile güncellenecek soru parçaları - component_status_change
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

        test = TestRepository(test=queryset)
        test.request = request

        # test için yer bir cevap sınıfı oluşturalım
        test.create_answer()

        # test cevapları için yeni bir unique oluşturalım
        test.answer.set_test_unique()

        # post edilen cevapları ekleyelim
        test.answer.answers = answers

        # test cevaplarını işleyelim
        test.answer.update_questions()
        test.answer.update_components()
        test.answer.update_test_result()

        return Response([])
