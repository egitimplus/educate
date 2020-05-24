from components.feeds import ComponentStatRepository
from questions.models import QuestionAnswerStat


class QuestionStatRepository:

    def __init__(self, request, **kwargs):
        self.request = request
        self.question = kwargs.pop("question", None)
        self.test_unique = kwargs.pop("test_unique", None)

    def add_true(self):
        c = list()

        for component in self.components:

            csr = ComponentStatRepository(
                request=self.request,
                component=component,
                question=self.question,
                test_unique=self.test_unique
            )

            true_components = csr.add_true_answer()
            c.append(component.id)

            for tc in true_components:
                c.append(tc)

        return c

    def add_false(self):
        c = list()

        for component in self.components:

            csr = ComponentStatRepository(
                request=self.request,
                component=component,
                question=self.question,
                test_unique=self.test_unique
            )

            csr.add_false_answer()

            # soru parçasını doğru soru parçası listesine ekleyelim
            c.append(component.id)

        return c

    def add_empty(self):
        c = list()

        for component in self.components:

            csr = ComponentStatRepository(
                request=self.request,
                component=component,
                question=self.question,
                test_unique=self.test_unique
            )

            csr.add_empty_answer()

            # soru parçasını doğru soru parçası listesine ekleyelim
            c.append(component.id)

        return c


