from rest_framework import viewsets, mixins, status
from tests.models import Test, TestUnique, TestQuestion
from tests.serializers import TestUniqueSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from educategories.serializers import EduCategorySimpleSerializer
from questions.serializers import QuestionSerializer


class TestUniqueViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = TestUnique.objects.all()
    serializer_class = TestUniqueSerializer

    '''
    # react 
    # -----------------------------------------------------------------------------------------------------------------
    # view()            : soru cevapları
    '''
    @action(methods=['GET'], detail=True)
    def view(self, request, pk=None):

        user = request.user
        user = 2

        queryset = TestUnique.objects.filter(test_id=pk, user=user).order_by('-id').first()

        response = []

        if queryset:
            answers = []
            if queryset.test_unique_stats:
                for a in queryset.test_unique_stats.filter(user=user):
                    answers.append(a)

            response = {
                'id': queryset.id,
                'test_id': queryset.test_id,
                'answers': answers
            }

        return Response(response)
