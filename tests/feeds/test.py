from tests.feeds import TestAnswerRepository
from library.mixins import TestUniqueMixin, RequestMixin


class TestRepository(TestUniqueMixin, RequestMixin):

    def __init__(self, **kwargs):
        self.__object = kwargs.pop("test", None)
        self.__answer = None

    def create_answer(self):
        self.__answer = TestAnswerRepository(test=self)

    @property
    def answer(self):
        return self.__answer

    @property
    def object(self):
        return self.__object

    def questions(self):
        return self.__object.questions.order_by('question').all()
