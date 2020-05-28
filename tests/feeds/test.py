from tests.feeds import TestAnswerRepository
from library.mixins import TestUniqueMixin, RequestMixin


class TestRepository(TestUniqueMixin, RequestMixin):
    _answer = None

    def __init__(self, **kwargs):
        self._object = kwargs.pop("test", None)

    def create_answer(self):
        self._answer = TestAnswerRepository(test=self)

    @property
    def answer(self):
        return self._answer

    @property
    def object(self):
        return self._object

    def questions(self):
        return self._object.questions.order_by('question').all()
