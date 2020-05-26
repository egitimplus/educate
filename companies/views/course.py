from rest_framework import viewsets, mixins, status
from companies.models import Classroom, SchoolStudent, SchoolTeacher, SchoolLessonTeacher, ClassroomLesson, ClassroomTeacher, ClassroomStudent
from companies.serializers import ClassroomSerializer
from curricula.serializers import LearningLectureStatSerializer, LearningUnitSerializerWithSubjects, LearningSubjectSerializer
from companies.permissions import ClassroomPermissionMixin
from rest_framework.response import Response
from curricula.models import LearningSubject, LearningUnit, LearningLectureStat
from django.db.models import Count
from components.models import ComponentStat
from components.serializers import ComponentStatSerializer


class CourseViewSet(ClassroomPermissionMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    '''
    # react 
    # -----------------------------------------------------------------------------------------------------------------
    # list()                : kurs listesi
    # course()              : kurs derleri ve üniteleri
    # course_unit()         : kurs ünitesi, konuları ve bölümleri
    # course_user()         : kullanıcının kayıtlı kursları
    # course_lecture_stat() : lecture okundu olarak düzenler
    # course_stat()         : kurs soru tiplerinin istatistikleri
    # course_lesson()       : kurs dersi, üniteleri ve konuları - kulllanılmıyor
    '''

    # sınıfa eklenmiş dersleri ve üniteleri listeler
    def course(self, request, pk=None):
        classroom = self.get_object()

        queryset = ClassroomLesson.objects.select_related(
            'lesson__lesson__curricula'
        ).prefetch_related(
            'lesson__lesson__curricula__units__component'
        ).filter(classroom=classroom).all()

        response = []
        item = {}
        content = {}

        for item in queryset:
            unit = LearningUnitSerializerWithSubjects(item.lesson.lesson.curricula.units.all(), many=True)

            components = list()

            for unit_item in item.lesson.lesson.curricula.units.all():
                unit_components = list(unit_item.component.values_list('id', flat=True))
                components = components + unit_components

            unique_components = list(set(components))

            response.append({
                'id': item.id,
                'period': item.lesson.duration,
                'name': item.lesson.name,
                'lesson_id': item.lesson.id,
                'lesson_name': item.lesson.lesson.name,
                'publisher_id': item.lesson.publisher_id,
                'curricula_id': item.lesson.lesson.curricula.id,
                'curricula_name': item.lesson.lesson.curricula.name,
                'unit': unit.data,
                'component': unique_components
            })

        if item:
            content = {
                'id': item.classroom.id,
                'name': item.classroom.name,
                'lessons': response
            }

        return Response(content)

    # kullanıcının kayıtlı olduğu kursları listeler
    def course_user(self, request):
        queryset = Classroom.objects.filter(student=request.user).all()
        ids = queryset.values_list('id', flat=True)

        return Response(ids)

    # kurs soru parçalarının istatistikleri
    def course_stat(self, request, pk=None):
        classroom = self.get_object()

        queryset = ClassroomLesson.objects.prefetch_related('lesson__lesson__curricula__units__component').filter(classroom=classroom).all()

        e = list()

        for q in queryset:
            for u in q.lesson.lesson.curricula.units.all():
                d = list(u.component.values_list('id', flat=True))
                e = e + d

        components = (list(set(e)))

        stats = ComponentStat.objects.filter(component__in=components, user=request.user).all()

        serializer = ComponentStatSerializer(stats, many=True)
        return Response(serializer.data)

    # seçilmiş olan dersin ünite ve konularını listeler
    def course_lesson(self, request, pk=None):
        publisher_id = int(self.request.query_params.get('publisher_id', None))
        lesson_id = int(self.request.query_params.get('lesson_id', None))

        row = ClassroomLesson.objects.select_related(
            'lesson__lesson__curricula'
        ).prefetch_related(
            'lesson__lesson__curricula__units'
        ).filter(pk=lesson_id).first()

        unit = LearningUnitSerializerWithSubjects(row.lesson.lesson.curricula.units.all(), many=True)

        response = {
            'id': row.id,
            'period': row.lesson.duration,
            'name': row.lesson.name,
            'lesson_id': row.lesson.id,
            'lesson_name': row.lesson.lesson.name,
            'publisher_id': row.lesson.publisher_id,
            'curricula_id': row.lesson.lesson.curricula.id,
            'curricula_name': row.lesson.lesson.curricula.name,
            'unit': unit.data
        }

        return Response(response)

    # seçilmiş olan ünitenin konularını ve bölümlerini listeler
    def course_unit(self, request, pk=None):
        publisher_id = int(self.request.query_params.get('p', None))
        unit_id = int(self.request.query_params.get('u', None))

        row = LearningUnit.objects.get(pk=unit_id)

        queryset = LearningSubject.objects.prefetch_related('lecture_parent').filter(
            unit_id=unit_id,
            lecture_parent__publisher_id=publisher_id
        ).annotate(total=Count('unit_id')).all()
        serializer = LearningSubjectSerializer(
            queryset, many=True, context={'request': request, 'publisher_id': publisher_id})

        data = {
            'id': row.id,
            'name': row.name,
            'subjects': serializer.data
        }

        return Response(data)

    # lecture okundu olarak düzenler
    def course_lecture_stat(self, request, pk=None):
        lecture_id = int(self.request.query_params.get('lc', None))

        obj, created = LearningLectureStat.objects.update_or_create(
            user=request.user,
            lecture_id=lecture_id,
            defaults={'lecture_status': 1},
        )

        serializer = LearningLectureStatSerializer(obj, many=False)
        return Response({'data': serializer.data})
