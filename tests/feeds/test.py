from tests.feeds import TestAnswerRepository


class TestRepository:

    def __init__(self, request, test):
        self.request = request
        self.test = test

    def answer(self):
        return TestAnswerRepository(request=self.request, test=self.test)

    def questions(self):
        return self.test.questions.order_by('question').all()
