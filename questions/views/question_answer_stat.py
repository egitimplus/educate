from rest_framework import viewsets, mixins
from questions.serializers import QuestionAnswerStatSerializer, QuestionAnswerStatPostSerializer
from questions.models import QuestionAnswerStat


class QuestionAnswerStatViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = QuestionAnswerStat.objects.all()
    serializer_class = QuestionAnswerStatSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return QuestionAnswerStatPostSerializer

        return QuestionAnswerStatSerializer
