from rest_framework import viewsets, mixins, status
from curricula.models import LearningDomain
from curricula.serializers import LearningDomainSerializer


class LearningDomainViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                            mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = LearningDomain.objects.all()
    serializer_class = LearningDomainSerializer
