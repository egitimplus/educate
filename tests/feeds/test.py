from tests.feeds import TestAnswerRepository
from library.mixins import TestUniqueMixin, RequestMixin


class TestRepository(TestUniqueMixin, RequestMixin):
    _answer = None

    def __init__(self, test):
        self._queryset = test

    def create_answer(self):
        self._answer = TestAnswerRepository(test=self)

    @property
    def answer(self):
        return self._answer

    @property
    def queryset(self):
        return self._queryset

    def questions(self):
        return self._queryset.questions.order_by('question').all()
