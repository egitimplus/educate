from companies.feeds import CourseAbstract
from companies.models import ClassroomLesson


class CourseSimpleRepository(CourseAbstract):

    def __init__(self, **kwargs):
        self.__parent = kwargs.pop("parent", None)

    def detail(self):
        item = ClassroomLesson.objects.select_related(
            'lesson__lesson__curricula', 'classroom'
        ).prefetch_related(
            'lesson__lesson__curricula__units__component',
            'lesson__lesson__curricula__units__subjects__lecture_parent',
        ).filter(classroom=self.__parent.object).first()

        units = item.lesson.lesson.curricula.units.all()
        unit_serializer = LearningUnitSerializer(units, many=True)

        components = list()

        for unit_item in units:
            unit_components = list(unit_item.component.values_list('id', flat=True))
            components = components + unit_components

        unique_components = list(set(components))

        content = {
            'id': item.classroom.id,
            'name': item.classroom.name,
            'lessons': {
                'id': item.id,
                'period': item.lesson.duration,
                'name': item.lesson.name,
                'lesson_id': item.lesson.id,
                'lesson_name': item.lesson.lesson.name,
                'publisher_id': item.lesson.publisher_id,
                'curricula_id': item.lesson.lesson.curricula.id,
                'curricula_name': item.lesson.lesson.curricula.name,
                'unit': unit_serializer.data,
                'component': unique_components
            }
        }

        return content

    def lesson(self):
        pass

    def stat(self):
        pass

    def unit(self):
        pass

    def lecture_stat(self):
        pass

    def lecture_stats(self):
        pass
