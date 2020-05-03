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
from components.models import ComponentAnswerStat


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

    @transaction.atomic
    @action(methods=['POST'], detail=False)
    def finish(self, request):
        answers = request.data.get('answers', None)
        test_id = request.data.get('test_id', None)

        if len(answers) < 1:
            return HttpResponseServerError("You must answer a question.")

        queryset = Test.objects.prefetch_related('questions', 'questions__component').get(id=test_id)

        test_unique = TestUnique.objects.create(
            user_id=request.user.id,
            test_id=queryset.id,
            report='report',
            test_result=0
        )

        questions = queryset.questions.order_by('question').all()

        total_questions = len(questions)
        true_questions = 0

        components = {
            'true': [],
            'false': []
        }

        for question in questions:
            question_components = question.component.all().values_list('id', flat=True)

            question_components_unique = list(set(question_components))
            question_components_unique.sort()

            question_code = '-'.join(map(str, question_components_unique))

            question_answer = question.answers.filter(is_true_answer=1).first()

            i = 0
            for answer in answers:
                if answer:
                    if answer['question_id'] == question.id:

                        i = i + 1
                        if answer['answer_id'] == question_answer.id:
                            for item in question_components:
                                components['true'].append(item)

                            true_questions = true_questions + 1

                            QuestionAnswerStat.objects.create(
                                answer_is_true=1,
                                answer_seconds=0,
                                answer_type=1,
                                question_id=question.id,
                                user_id=request.user.id,
                                test_unique_id=test_unique.id,
                                question_answer_id=question_answer.id,
                                answer_count=1
                            )

                            obj, created = QuestionUnique.objects.get_or_create(
                                question_code=question_code
                            )

                            # status belirlenmesi lazım
                            # answers alanı iptal edelim.

                            QuestionUniqueStat.objects.update_or_create(
                                question_unique_id=obj.id,
                                user_id=request.user.id,
                                question_code=question_code,
                                defaults={"status": 1}
                            )

                        else:
                            for item in question_components:
                                components['false'].append(item)

                            QuestionAnswerStat.objects.create(
                                answer_is_true=0,
                                answer_seconds=0,
                                answer_type=1,
                                question_id=question.id,
                                user_id=request.user.id,
                                test_unique_id=test_unique.id,
                                question_answer_id=question_answer.id,
                                answer_count=1
                            )

                            obj, created = QuestionUnique.objects.get_or_create(
                                question_code=question_code
                            )

                            # status belirlenmesi lazım
                            # answers alanı iptal edelim.

                            QuestionUniqueStat.objects.update_or_create(
                                question_unique_id=obj.id,
                                user_id=request.user.id,
                                question_code=question_code,
                                defaults={"status": 0}
                            )

            if i == 0:
                for component in question_components:
                    ComponentAnswerStat.objects.create(
                        component_id=component,
                        question_id=question.id,
                        test_unique_id=test_unique.id,
                        user_id=request.user.id,
                        answer_is_true=0,
                        answer_is_empty=1
                    )

        test_result = math.ceil((true_questions/total_questions) * 100)

        if test_result > 100:
            test_result = 100

        print(components)
        return HttpResponseServerError("You must answer a question.")

        TestUnique.objects.filter(id=test_unique.id).update(test_result=test_result)

        return Response([])






