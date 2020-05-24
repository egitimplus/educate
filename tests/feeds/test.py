from tests.feeds import TestAnswerRepository


class TestRepository:

    def __init__(self, request, test):
        self._request = request
        self._queryset = test

    def answer(self):
        return TestAnswerRepository(request=self._request, test=self._queryset)

    def questions(self):
        return self._queryset.questions.order_by('question').all()
