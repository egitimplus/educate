from rest_framework import viewsets, mixins, status
from curricula.models import LearningUnit, LearningSubject
from curricula.serializers import LearningSubjectSerializer, LearningUnitSerializer, LearningUnitSimpleSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class LearningUnitViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):

    queryset = LearningUnit.objects.all()
    serializer_class = LearningUnitSerializer

    # uniteye bağlı konu listesi
    @action(methods=['GET'], detail=True)
    def subject_list(self, request, pk=None):
        queryset = LearningSubject.objects.filter(unit_id=pk).all()

        serializer = LearningSubjectSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    # kullanıcı ünite listesi
    @action(methods=['GET'], detail=True)
    def info(self, request, pk=None):
        unit_queryset = LearningUnit.objects.filter(id=pk).first()
        subject_queryset = LearningSubject.objects.filter(unit_id=pk).all()

        unit = LearningUnitSerializer(unit_queryset, many=False)
        subject = LearningSubjectSerializer(subject_queryset, many=True)

        data = {
            'unit': unit.data,
            'subjects': subject.data
        }

        return Response(data)

    # ünite detayı
    @action(methods=['GET'], detail=True)
    def view(self, request, pk=None):
        queryset = LearningUnit.objects.filter(id=pk).first()
        serializer = LearningUnitSimpleSerializer(queryset, many=False)

        return Response(serializer.data)

    # ünite test ekler
    @action(methods=['POST'], detail=True)
    def attach_test(self, request, pk=None):
        unit = LearningUnit.objects.filter(id=pk).first()

        try:
            test = unit.test.create(name=request.data.get('name'), content=request.data.get('content'), test_id=request.data.get('test_id'), position=0)

            return Response('Test Eklendi', status=status.HTTP_200_OK)

        except Exception as e:
            return Response('Test Eklenemedi', status=status.HTTP_400_BAD_REQUEST)

    # ders görüntüleme
    @action(methods=['GET'], detail=True)
    def user_view(self, request, pk=None):

        queryset = LearningUnit.objects.select_related('lesson').prefetch_related(
            'learningsubject_set', 'learningsubject_set__lecture_parent'
        ).filter(id=pk).first()

        if queryset:
            subject = LearningSubjectSerializer(queryset.learningsubject_set.order_by('position').all(),
                                                many=True,
                                                context={'request': request})

            data = {
                'lesson': {
                    'id': queryset.lesson.id,
                    'name': queryset.lesson.name,
                    'duration': queryset.lesson.duration
                },
                'unit': {
                    'id': queryset.id,
                    'name': queryset.name
                },
                'subjects': subject.data,
            }

            return Response(data)

        return Response({'error': 'Ünite bulunamadı.'}, status=status.HTTP_400_BAD_REQUEST)
