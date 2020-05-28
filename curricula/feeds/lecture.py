from components.feeds import ComponentMixin
from library.mixins import RequestMixin


class LectureRepository(ComponentMixin, RequestMixin):

    def __init__(self, **kwargs):
        self._queryset = kwargs.pop("lecture", None)
