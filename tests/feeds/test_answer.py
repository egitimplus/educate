from tests.models import Test, TestUnique
import math
from library.feeds import flatten


class TestAnswerRepository:

    def __init__(self, request, test):
        self.request = request
        self.test = test
        self.test_unique = self.create_test_answer()

        self.true_question = 0
        self.false_question = 0
        self.empty_question = 0
        self.total_question = 0

        self.true_components = []
        self.false_components = []
        self.empty_components = []

    def create_test_answer(self):
        test_unique = TestUnique.objects.create(
            user_id=self.request.user.id,
            test_id=self.test.id,
            report='report',
            test_result=0
        )

        return test_unique

    def test_result(self):
        result = math.ceil((self.true_question / self.total_question) * 100)

        if result > 100:
            result = 100

        return result

    def all_components(self):
        all_components = self.true_components + self.false_components + self.empty_components

        return list(set(flatten(all_components)))
