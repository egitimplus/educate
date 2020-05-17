from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.db import transaction
from components.models import Component
from components.serializers import ComponentSerializer, ComponentPostSerializer
from components.feeds import ComponentRepository
from rest_framework.decorators import action
from library.feeds import get_breadcrumb, get_category


class ComponentViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin,
                       mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs['pk']

        queryset = Component.objects.filter(id=pk).prefetch_related('to_component', 'source_component').first()

        cr = ComponentRepository(request=request, component=queryset)

        cr.sub_components()
        cr.all_sub_components()
        cr.parent_components()
        cr.data_components()

        all_components = cr.component_formats(
            sub_components='list',
            all_sub_components='list',
            parent_components='list',
            data_components='dict',
            all_components='list'
        )

        serialized_question = ComponentSerializer(queryset)
        response = serialized_question.data
        response.update(all_components)

        return Response(response)

    @action(methods=['GET'], detail=True)
    def user_detail(self, request, pk=None):

        queryset = Component.objects.filter(id=pk).prefetch_related(
            'to_component',
            'component_answer_stat_component',
            'component_stat_component'
        ).first()

        serialized_component = ComponentSerializer(queryset)

        stats = queryset.component_stat_component.first()
        component_status = stats.component_status if status else 0
        component_count = queryset.component_answer_stat_component.count()

        cr = ComponentRepository(request=request, component=queryset, counts=True, status=True)

        cr.sub_components()
        cr.all_sub_components()

        all_components = cr.component_formats(
            sub_components='dict',
            all_sub_components='dict'
        )

        response = serialized_component.data
        response.update({
            'sub_components': all_components['sub_components'],
            'all_sub_components': all_components['all_sub_components'],
            'category': get_category(queryset.edu_category_id),
            'stats': {
                'status': component_status,
                'count': component_count
            },
        })

        return Response(response)

    @action(methods=['POST'], detail=False)
    def search(self, request):

        response = []

        # TODO post işlemleri
        queryset = Component.objects.prefetch_related('to_component').filter(name__icontains=request.data.get('word')).all()

        for query in queryset:

            serialized_question = ComponentSerializer(query)
            item = serialized_question.data

            cr = ComponentRepository(request=request, component=query)

            cr.sub_components()
            cr.all_sub_components()
            cr.parent_components()

            all_components = cr.component_formats(
                sub_components='list',
                all_sub_components='list',
                parent_components='list',
                all_components='list'
            )

            item.update(all_components)

            response.append(item)

        return Response(response)

    @action(methods=['GET'], detail=True)
    def parents(self, request, pk=None):
        question = Component.objects.values_list('edu_category_id', flat=True).filter(id=pk).first()
        categories = get_breadcrumb(question)
        return Response(categories)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = ComponentPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ComponentPostSerializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
