from rest_framework import viewsets, mixins
from publishers.models import Publisher, Book
from publishers.serializers import PublisherSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from library.feeds import DisableSignals


class PublisherViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    # yayınevine bağlı kitap listesi
    def book_list(self, request, pk=None):
        queryset = Book.objects.filter(publisher_id=pk).all()
        self.get_object()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = BookSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def manager_list(self, request, pk=None):
        self.get_object()
        queryset = Publisher.objects.prefetch_related('manager').filter(id=pk).first()

        response = []
        for data in queryset.publishermanager_set.all():
            response.append({
                'publisher_manager_id': data.id,
                'id': data.manager.id,
                'first_name': data.manager.first_name,
                'last_name': data.manager.last_name,
                'email': data.manager.email,
                'username': data.manager.username
            })
        return Response(response)

    def update_publisher(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        instance.name = request.data.get('name')

        with DisableSignals():
            instance.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
