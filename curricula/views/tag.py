from rest_framework import viewsets, mixins, status
from curricula.models import LearningTag
from curricula.serializers import LearningTagSerializer


class LearningTagViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                         mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = LearningTag.objects.all()
    serializer_class = LearningTagSerializer

