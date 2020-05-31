from companies.feeds import CourseAbstract
from companies.models import ClassroomLesson
from curricula.serializers import LearningUnitSerializerWithSubjects
from components.models import ComponentStat
from components.serializers import ComponentStatSerializer
from curricula.models import LearningUnit, LearningSubject, LearningLectureStat
from curricula.serializers import LearningSubjectSerializer, LearningLectureStatSerializer
from django.db.models import Count


class CourseDetailRepository(CourseAbstract):

    def __init__(self, **kwargs):
        self.__parent = kwargs.pop("parent", None)

    def detail(self):
        queryset = ClassroomLesson.objects.select_related(
            'lesson__lesson__curricula', 'classroom'
        ).prefetch_related(
            'lesson__lesson__curricula__units__component'
        ).filter(classroom=self.__parent.object).all()

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

        return content

    def lesson(self):
        row = ClassroomLesson.objects.select_related(
            'lesson__lesson__curricula'
        ).prefetch_related(
            'lesson__lesson__curricula__units'
        ).filter(pk=self.__parent.lesson_id).first()

        unit = LearningUnitSerializerWithSubjects(row.lesson.lesson.curricula.units.all(), many=True)

        return {
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

    def stat(self):
        queryset = ClassroomLesson.objects.prefetch_related('lesson__lesson__curricula__units__component').filter(
            classroom=self.__parent.object).all()

        e = list()

        for q in queryset:
            for u in q.lesson.lesson.curricula.units.all():
                d = list(u.component.values_list('id', flat=True))
                e = e + d

        components = (list(set(e)))

        stats = ComponentStat.objects.filter(component__in=components, user=self.__parent.request.user).all()

        serializer = ComponentStatSerializer(stats, many=True)

        return serializer.data

    def unit(self):

        row = LearningUnit.objects.get(pk=self.__parent.unit_id)

        queryset = LearningSubject.objects.prefetch_related('lecture_parent').filter(
            unit_id=self.__parent.unit_id,
            lecture_parent__publisher_id=self.__parent.publisher_id
        ).annotate(total=Count('unit_id')).all()

        serializer = LearningSubjectSerializer(
            queryset, many=True, context={
                'request': self.__parent.request, 'publisher_id': self.__parent.publisher_id
            })

        return {
            'id': row.id,
            'name': row.name,
            'subjects': serializer.data
        }

    def lecture_stat(self):

        obj, created = LearningLectureStat.objects.update_or_create(
            user=self.__parent.request.user,
            lecture_id=self.__parent.lecture_id,
            defaults={'lecture_status': 1},
        )

        serializer = LearningLectureStatSerializer(obj, many=False)

        return serializer.data
