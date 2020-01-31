from rest_framework import viewsets, mixins, status
from curricula.models import LearningLecture, LearningLectureStat
from curricula.serializers import LearningLectureSerializer, LearningLecturePostSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from components.feeds import ComponentPartRepository
from django.db import transaction


class LearningLectureViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                            mixins.UpdateModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):

    queryset = LearningLecture.objects.all()
    serializer_class = LearningLectureSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Soru ayrıntıları
        TODO File, Domain, Path eklenecek.
        """
        pk = self.kwargs['pk']

        queryset = LearningLecture.objects.filter(id=pk).prefetch_related(
            'component',
            'component__source_component',
            'content_object'
        ).select_related('practice').first()

        serializer = LearningLectureSerializer(queryset, many=False, context={'request': request})
        response = serializer.data

        lecture_repo = ComponentPartRepository(request, queryset)

        response.update({
            'all_sub_components':  lecture_repo.all_sub_components(return_format='list'),
            'sub_components': lecture_repo.sub_components(return_format='list'),
            'data_components': lecture_repo.data_sub_components(),
            'all_data_components': lecture_repo.data_all_sub_components()
        })

        return Response(response)

    # bölüm listesi
    @action(methods=['GET'], detail=True)
    def info(self, request, pk=None):
        queryset = LearningLecture.objects.filter(subject=pk).all()
        self.get_object()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = LearningLectureSerializer(queryset, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = LearningLectureSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = LearningLecturePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.save()
        return Response(question, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = LearningLecturePostSerializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response([])

    @action(methods=['GET'], detail=True)
    def update_lecture_view(self, request, pk=None):

        user_id = request.user.id

        queryset = LearningLectureStat.objects.filter(lecture=pk).first()

        if queryset:

            queryset.lecture_status = 1
            queryset.save()

        else:

            item = LearningLectureStat(user_id=user_id, lecture_id=pk, lecture_status=1)
            item.save()

        return Response([], status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=True)
    def update_lecture_practice(self, request, pk=None):

        user_id = request.user.id

        queryset = LearningLectureStat.objects.filter(lecture=pk).first()

        if queryset:

            queryset.practice_status = 1
            queryset.save()

        else:

            item = LearningLectureStat(user_id=user_id, lecture_id=pk, practice_status=1)
            item.save()

        return Response([], status=status.HTTP_201_CREATED)

