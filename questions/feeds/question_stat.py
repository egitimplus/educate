from components.feeds import ComponentRepository
from library.mixins import TestUniqueMixin, RequestMixin


class QuestionStatRepository(TestUniqueMixin, RequestMixin):

    def __init__(self, **kwargs):
        self.__question = kwargs.pop("question", None)
        self.__test_unique = self.__question.test_unique
        self.__request = self.__question.request

    def add_true(self):
        components = list()

        for component in self.__question.components:
            c = ComponentRepository(component=component)
            c.request = self.__request
            c.test_unique = self.__test_unique
            c.create_stat()
            c.stat.question = self.__question
            components.append(component.id)

            for true_component in c.stat.add_true():
                components.append(true_component)

        return components

    def add_false(self):
        components = list()

        for component in self.__question.components:
            c = ComponentRepository(component=component)
            c.request = self.__question.request
            c.request = self.__request
            c.test_unique = self.__test_unique
            c.create_stat()
            c.stat.add_false()

            # soru parçasını doğru soru parçası listesine ekleyelim
            components.append(component.id)

        return components

    def add_empty(self):
        components = list()

        for component in self.__question.components:

            c = ComponentRepository(component=component)
            c.request = self.__request
            c.test_unique = self.__test_unique
            c.create_stat()
            c.stat.question = self.__question
            c.stat.add_empty()

            # soru parçasını doğru soru parçası listesine ekleyelim
            components.append(component.id)

        return components


