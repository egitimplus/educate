from library.mixins import RequestMixin
from companies.feeds import CourseDetailRepository, CourseSimpleRepository


class CourseRepository(RequestMixin):

    __course = None
    __lecture_id = None
    __publisher_id = None
    __unit_id = None
    __lesson_id = None

    def __init__(self, **kwargs):
        self.__object = kwargs.pop("course", None)

        if self.__object is not None:
            self.create_repository()

    def create_repository(self):
        if self.__object.type == 1:
            self.__course = CourseDetailRepository(parent=self)
        else:
            self.__course = CourseSimpleRepository(parent=self)

    @property
    def object(self):
        return self.__object

    @property
    def unit_id(self):
        return self.__unit_id

    @unit_id.setter
    def unit_id(self, value):
        self.__unit_id = value

    @property
    def lecture_id(self):
        return self.__lecture_id

    @lecture_id.setter
    def lecture_id(self, value):
        self.__lecture_id = value

    @property
    def publisher_id(self):
        return self.__publisher_id

    @publisher_id.setter
    def publisher_id(self, value):
        self.__publisher_id = value

    @property
    def lesson_id(self):
        return self.__lesson_id

    @lesson_id.setter
    def lesson_id(self, value):
        self.__lesson_id = value

    def lesson(self):
        return self.__course.lesson()

    def detail(self):
        return self.__course.detail()

    def stat(self):
        return self.__course.stat()

    def unit(self):
        return self.__course.unit()

    def lecture_stat(self):
        return self.__course.lecture_stat()
