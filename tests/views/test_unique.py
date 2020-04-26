from rest_framework import viewsets, mixins, status
from tests.models import TestUnique
from tests.serializers import TestUniqueSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


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

        queryset = TestUnique.objects.filter(test_id=pk, user=user).order_by('-id').first()

        response = []

        if queryset:
            answers = []
            if queryset.test_unique_stats:
                for a in queryset.test_unique_stats.filter(user=user):
                    answers.append({
                        'id': a.id,
                        'answer_is_true': a.answer_is_true,
                        'question_id': a.question_id,
                        'question_answer_id': a.question_answer_id,
                        'test_unique_id': a.test_unique_id,
                        'answer_count': a.answer_count
                    })

            response = {
                'id': queryset.id,
                'test_id': queryset.test_id,
                'answers': answers,
                'test_result': queryset.test_result
            }

        return Response(response)
