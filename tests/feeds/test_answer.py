from tests.models import TestUnique
import math
from library.feeds import flatten


class TestAnswerRepository:

    def __init__(self, request, test):
        self.request = request
        self.queryset = test
        self.test_unique = self.create_test_answer()

        self.counts = {
            'true': 0,
            'false': 0,
            'empty': 0,
            'total': 0,
        }

        self.components = {
            'true': [],
            'false': [],
            'empty': [],
        }

    def create_test_answer(self):
        test_unique = TestUnique.objects.create(
            user_id=self.request.user.id,
            test_id=self.queryset.id,
            report='report',
            test_result=0
        )

        return test_unique

    def test_result(self):
        result = math.ceil((self.counts['true'] / self.counts['total']) * 100)

        if result > 100:
            result = 100

        return result

    def all_components(self):
        all_components = self.components['true'] + self.components['false'] + self.components['empty']

        return list(set(flatten(all_components)))
