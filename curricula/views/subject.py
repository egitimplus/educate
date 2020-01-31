from rest_framework import viewsets, mixins, status
from curricula.models import LearningSubject, LearningLecture
from curricula.serializers import LearningSubjectSerializer, LearningSubjectSimpleSerializer, LearningLectureSerializer, LearningLectureUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class LearningSubjectViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                            mixins.UpdateModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):

    queryset = LearningSubject.objects.all()
    serializer_class = LearningSubjectSerializer

    # kullanıcı konu listesi
    @action(methods=['GET'], detail=True)
    def info(self, request, pk=None):
        subject_queryset = LearningSubject.objects.filter(id=pk).first()
        lecture_queryset = LearningLecture.objects.filter(subject=pk).all()

        subject = LearningSubjectSerializer(subject_queryset, many=False)
        lecture = LearningLectureUserSerializer(lecture_queryset, many=True,  context={'request': request})

        data = {
            'subject': subject.data,
            'lectures': lecture.data
        }

        return Response(data)

    # konuya bağlı bölüm listesi
    @action(methods=['GET'], detail=True)
    def lecture_list(self, request, pk=None):

        publisher_id = request.query_params.get('publisher_id')
        queryset = LearningLecture.objects.filter(subject_id=pk, publisher_id=publisher_id).order_by('position').all()
        serializer = LearningLectureSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    # kullanıcı ünite listesi
    @action(methods=['GET'], detail=True)
    def view(self, request, pk=None):
        queryset = LearningSubject.objects.filter(id=pk).first()
        serializer = LearningSubjectSimpleSerializer(queryset, many=False)

        return Response(serializer.data)

    # konuya test ekler
    @action(methods=['POST'], detail=True)
    def attach_test(self, request, pk=None):
        subject = LearningSubject.objects.filter(id=pk).first()

        try:
            test = subject.test.create(name=request.data.get('name'), content=request.data.get('content'), test_id=request.data.get('test_id'), position=0)

            return Response('Test Eklendi', status=status.HTTP_200_OK);

        except Exception as e:
            return Response('Test Eklenemedi', status=status.HTTP_400_BAD_REQUEST)

        # ders görüntüleme

    @action(methods=['GET'], detail=True)
    def user_view(self, request, pk=None):

        queryset = LearningSubject.objects.select_related('unit__lesson').prefetch_related(
            'lecture_parent'
        ).filter(id=pk).first()

        if queryset:
            lecture = LearningLectureSerializer(queryset.lecture_parent.order_by('position').all(), many=True, context={'request': request})

            data = {
                'lesson': {
                    'id': queryset.unit.lesson.id,
                    'name': queryset.unit.lesson.name
                },
                'unit': {
                    'id': queryset.unit.id,
                    'name': queryset.unit.name
                },
                'subject': {
                    'id': queryset.id,
                    'name': queryset.name
                },
                'lectures': lecture.data,
            }

            return Response(data)

        return Response('Ders bulunamadı.', status=status.HTTP_400_BAD_REQUEST)