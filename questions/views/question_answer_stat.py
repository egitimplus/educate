from rest_framework import viewsets, mixins
from questions.serializers import QuestionAnswerStatSerializer
from questions.models import QuestionAnswerStat


class QuestionAnswerStatViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = QuestionAnswerStat.objects.all()
    serializer_class = QuestionAnswerStatSerializer

