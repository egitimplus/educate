from components.feeds import ComponentMixin
from library.mixins import RequestMixin


class LectureRepository(ComponentMixin, RequestMixin):

    def __init__(self, **kwargs):
        self.__object = kwargs.pop("lecture", None)
