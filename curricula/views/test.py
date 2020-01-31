from rest_framework import viewsets, mixins, status
from curricula.models import LearningTest
from curricula.serializers import LearningTestSerializer, LearningTestUniqueSerializer


class LearningTestViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = LearningTest.objects.all()
    serializer_class = LearningTestSerializer
