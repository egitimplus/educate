from rest_framework import viewsets, mixins, status
from tests.models import Test
from tests.serializers import TestSerializer, TestPostSerializer, SimpleTestSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class TestViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return TestPostSerializer

        return TestSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TestSerializer(instance)

        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def view(self, request, pk=None):
        queryset = Test.objects.prefetch_related('questions','categories').filter(id=pk).first()

        questions = []
        categories = []

        for question in queryset.question.all():
            questions.add(question)

        for category in queryset.edu_category.all():
            categories.add(category)

        response = {
            'id': queryset.id,
            'name': queryset.name,
            'test_seconds': queryset.test_seconds,
            'active': queryset.active,
            'questions': questions,
            'categories': categories
        }
        return Response(response)

    @action(methods=['POST'], detail=False)
    def search(self, request):
        # TODO publisher yetkisi var mı bakılmalı
        publisher = request.data.get('publisher_id', None)
        search_text = request.data.get('search_text', None)

        if not publisher:
            return Response('Yayınevi bulunamadı.', status=status.HTTP_400_BAD_REQUEST)

        queryset = Test.objects.filter(publisher_id=publisher)

        if search_text:
            queryset = queryset.filter(name__icontains=search_text)

        serializer = SimpleTestSerializer(queryset, many=True)

        return Response(serializer.data)
