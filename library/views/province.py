from rest_framework import viewsets, mixins
from library.models import Province
from library.serializers import ProvinceSerializer


class ProvinceViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):

    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


