from library.mixins import RequestMixin


class ClassroomRepository(RequestMixin):

    def __init__(self, **kwargs):
        self._queryset = kwargs.pop("classroom", None)

    def teacher_ids(self):
        return self._queryset.teacher.all().values_list('id', flat=True)




