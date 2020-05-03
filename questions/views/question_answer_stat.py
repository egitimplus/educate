from rest_framework import viewsets, mixins, status
from questions.serializers import QuestionAnswerStatSerializer, QuestionAnswerStatPostSerializer
from questions.models import QuestionAnswerStat
from rest_framework.response import Response


class QuestionAnswerStatViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = QuestionAnswerStat.objects.all()
    serializer_class = QuestionAnswerStatSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return QuestionAnswerStatPostSerializer

        return QuestionAnswerStatSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
