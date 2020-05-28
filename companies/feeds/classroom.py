from library.mixins import RequestMixin


class ClassroomRepository(RequestMixin):

    def __init__(self, **kwargs):
        self._queryset = kwargs.pop("classroom", None)

    @property
    def teachers(self):
        return self._queryset.teacher.all()




