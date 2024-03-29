from components.models import ComponentAnswerStat
from library.mixins import TestUniqueMixin, RequestMixin


class ComponentStatRepository(TestUniqueMixin, RequestMixin):

    def __init__(self, **kwargs):

        self._component = kwargs.pop("component", None)
        self._test_unique = self._component.test_unique
        self._request = self._component.request
        self._true_answer = 0
        self._empty_answer = 0
        self._question = None

    def add_answer(self, component=None):

        if component is None:
            component = self._component.object

        # cevabı soru parçası istatistiklerine ekleyelim
        ComponentAnswerStat.objects.create(
            component=component,
            question=self._question.object,
            test_unique=self._test_unique,
            user=self._request.user,
            answer_is_true=self._true_answer,
            answer_is_empty=self._empty_answer
        )

    def add_true(self):

        self._true_answer = 1
        self._empty_answer = 0

        # cevabı soru parçası istatistiklerine ekleyelim
        self.add_answer(self._component.object)

        self._component.all_sub_components()

        data = self._component.component_formats(all_sub_components='list')

        for component in data['all_sub_components']:
            self.add_answer(component)

        return data['all_sub_components']

    def add_false(self):

        self._true_answer = 0
        self._empty_answer = 0

        # cevabı soru parçası istatistiklerine ekleyelim
        self.add_answer()

        return self._component.object.id

    def add_empty(self):
        self._true_answer = 0
        self._empty_answer = 1

        # cevabı soru parçası istatistiklerine ekleyelim
        self.add_answer()

        return self._component.object.id

    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
