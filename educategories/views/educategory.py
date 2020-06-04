from rest_framework import viewsets, mixins, status
from educategories.models import EduCategory
from components.models import Component
from tests.models import Test
from components.serializers import ComponentSerializer
from educategories.serializers import EduCategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from components.feeds import ComponentRepository
from tests.serializers import TestSerializer


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = EduCategory.objects.all()
    serializer_class = EduCategorySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.depth == 0:
            EduCategory.objects.filter(lesson_id=instance.id).delete()
        elif instance.depth == 1:
            EduCategory.objects.filter(unit_id=instance.id).delete()
        elif instance.depth == 2:
            EduCategory.objects.filter(subject_id=instance.id).delete()

        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['GET'], detail=False)
    def lessons(self, request):
        queryset = EduCategory.objects.filter(depth=0).all()

        serializer = EduCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def subs(self, request, pk=None):
        queryset = EduCategory.objects.filter(parent_id=pk).all()

        serializer = EduCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def components(self, request, pk=None):
        response = []

        queryset = Component.objects.prefetch_related('to_component','source_component').filter(edu_category_id=pk).all()

        for query in queryset:
            serialized_question = ComponentSerializer(query)
            item = serialized_question.data

            cr = ComponentRepository(component=query)
            cr.request = request

            cr.sub_components()
            cr.all_sub_components()
            cr.parent_components()

            all_components = cr.component_formats(
                sub_components='list',
                all_sub_components='list',
                parent_components='list',
                all_components='list',
                data_components='dict'
            )

            item.update(all_components)

            response.append(item)

        return Response(response)

    @action(methods=['GET'], detail=True)
    def tests(self, request, pk=None):
        queryset = Test.objects.filter(categories__id=pk).all()

        serializer = TestSerializer(queryset, many=True, context={'simple': True})
        return Response(serializer.data)
