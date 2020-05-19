from tests.feeds import TestAnswerRepository


class TestRepository:

    def __init__(self, request, test):
        self.request = request
        self.queryset = test

    def answer(self):
        return TestAnswerRepository(request=self.request, test=self.model)

    def questions(self):
        return self.queryset.questions.order_by('question').all()
