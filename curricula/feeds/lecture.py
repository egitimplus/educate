from components.feeds import ComponentMixin
from library.mixins import RequestMixin


class LectureRepository(ComponentMixin, RequestMixin):

    def __init__(self, **kwargs):
        self._object = kwargs.pop("lecture", None)
