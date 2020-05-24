from components.models import ComponentAnswerStat
from . import ComponentRepository


class ComponentStatRepository:

    def __init__(self, request, **kwargs):
        self.request = request

        self.queryset = kwargs.pop("component", None)
        self.question = kwargs.pop("question", None)
        self.test_unique = kwargs.pop("test_unique", None)

    def add_answer(self, component, answer):

        answer_is_true = 0
        answer_is_empty = 1

        if answer == 'true':
            answer_is_true = 1
            answer_is_empty = 0
        elif answer == 'false':
            answer_is_true = 0
            answer_is_empty = 0

        # cevabı soru parçası istatistiklerine ekleyelim
        ComponentAnswerStat.objects.create(
            component=component,
            question=self.question,
            test_unique=self.test_unique,
            user=self.request.user,
            answer_is_true=answer_is_true,
            answer_is_empty=answer_is_empty
        )

    def add_true_answer(self):

        # cevabı soru parçası istatistiklerine ekleyelim
        self.add_answer(self.queryset, 'true')

        cr = ComponentRepository(request=self.request, component=self.queryset)

        cr.all_sub_components()

        data = cr.component_formats(all_sub_components='list')

        for component in data['all_sub_components']:
            self.add_answer(component, 'true')

        return data['all_sub_components']

    def add_false_answer(self):
        # cevabı soru parçası istatistiklerine ekleyelim
        self.add_answer(self.queryset, 'false')

    def add_empty_answer(self):
        # cevabı soru parçası istatistiklerine ekleyelim
        self.add_answer(self.queryset, 'true')
