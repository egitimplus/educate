from rest_framework import viewsets, mixins, status
from companies.models import CompanyGroup, School
from publishers.models import Publisher
from companies.serializers import CompanyGroupSerializer, SchoolSerializer
from publishers.serializers import PublisherSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from companies.permissions import GroupPermissionMixin


class CompanyGroupViewSet(GroupPermissionMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):

    queryset = CompanyGroup.objects.all()
    serializer_class = CompanyGroupSerializer

    # gruba bağlı okul listesi
    @action(methods=['GET'], detail=True)
    def school_list(self, request, pk=None):

        user = request.user

        queryset = School.objects.filter(group_id=pk).all()
        self.get_object()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = SchoolSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SchoolSerializer(queryset, many=True)
        return Response(serializer.data)

    # gruba bağlı yayınevi listesi
    @action(methods=['GET'], detail=True)
    def publisher_list(self, request, pk=None):
        queryset = Publisher.objects.filter(group_id=pk).all()
        self.get_object()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PublisherSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PublisherSerializer(queryset, many=True)
        return Response(serializer.data)
