from rest_framework import viewsets, mixins
from library.models import Media
from library.serializers import MediaSerializer


class MediaViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):

    queryset = Media.objects.all()
    serializer_class = MediaSerializer


