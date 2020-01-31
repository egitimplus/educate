from rest_framework import viewsets, mixins
from publishers.models import Source
from publishers.serializers import SourcePostSerializer, SourceSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class SourceViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                            mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = Source.objects.all()
    serializer_class = SourceSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return SourcePostSerializer

        return SourceSerializer

    @action(methods=['GET'], detail=True)
    def children(self, request, pk=None):
        queryset = Source.objects.filter(parent_id=pk).all()
        serializer = SourceSerializer(queryset, many=True)

        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def questions(self, request, pk=None):
        queryset = Source.objects.prefetch_related('question').filter(id=pk).first()

        ids = set()

        for question in queryset.question.all():
            ids.add(question.id)

        return Response(ids)

    @action(methods=['POST'], detail=True)
    def change_questions(self, request, pk=None):

        source = Source.objects.filter(id=pk).first()

        for a in request.data.get('add'):
            source.question.add(a)

        for d in request.data.get('del'):
            source.question.remove(d)

        return Response([])

    @action(methods=['GET'], detail=True)
    def check_source(self, request, pk=None):
        queryset = Source.objects.prefetch_related('question').filter(id=pk).first()
        count = queryset.question.count()

        if count > 0:
            status = 1
        else:
            status = 0

        return Response({'id': pk, 'status': status})

