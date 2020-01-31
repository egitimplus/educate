from rest_framework import viewsets, mixins
from library.models import Exam
from library.serializers import ExamSerializer


class ExamViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):

    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


