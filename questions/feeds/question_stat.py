from components.feeds import ComponentRepository
from library.mixins import TestUniqueMixin, RequestMixin


class QuestionStatRepository(TestUniqueMixin, RequestMixin):

    def __init__(self, **kwargs):
        self._question = kwargs.pop("question", None)

    def add_true(self):
        components = list()

        for component in self._question.components:
            c = ComponentRepository(component=component)
            c.request = self._question.request

            c.create_stat()

            c.stat.request = self._question.request
            c.stat.test_unique = self._question.test_unique
            c.stat.question = self._question

            components.append(component.id)

            for true_component in c.stat.add_true():
                components.append(true_component)

        return components

    def add_false(self):
        components = list()

        for component in self._question.components:
            c = ComponentRepository(component=component)
            c.request = self._question.request

            c.create_stat()

            c.stat.request = self._question.request
            c.stat.test_unique = self._question.test_unique

            c.stat.add_false()

            # soru parçasını doğru soru parçası listesine ekleyelim
            components.append(component.id)

        return components

    def add_empty(self):
        components = list()

        for component in self._question.components:

            c = ComponentRepository(component=component)
            c.request = self._question.request

            c.stat.request = self._question.request
            c.stat.test_unique = self._question.test_unique

            c.create_stat()
            c.stat.add_empty()

            # soru parçasını doğru soru parçası listesine ekleyelim
            components.append(component.id)

        return components


