from components.models import ComponentAnswerStat
from . import ComponentRepository


class ComponentStatRepository:

    def __init__(self, request, component):
        self.component = component
        self.request = request

    def add_true_answer(self, **kwargs):
        question = kwargs.pop("question", None)
        test_unique = kwargs.pop("test_unique", None)

        # cevabı soru parçası istatistiklerine ekleyelim
        ComponentAnswerStat.objects.create(
            component=self.component,
            question=question,
            test_unique=test_unique,
            user=self.request.user,
            answer_is_true=1,
            answer_is_empty=0
        )

        cr = ComponentRepository(request=self.request, component=self.component)

        cr.all_sub_components()

        data = cr.component_formats(all_sub_components='list')

        for component in data['all_sub_components']:
            ComponentAnswerStat.objects.create(
                component_id=component,
                question=question,
                test_unique=test_unique,
                user=self.request.user,
                answer_is_true=1,
                answer_is_empty=0
            )

        return data['all_sub_components']

    def add_false_answer(self, **kwargs):
        question = kwargs.pop("question", None)
        test_unique = kwargs.pop("test_unique", None)

        # cevabı soru parçası istatistiklerine ekleyelim
        ComponentAnswerStat.objects.create(
            component=self.component,
            question=question,
            test_unique=test_unique,
            user=self.request.user,
            answer_is_true=0,
            answer_is_empty=0
        )

        return self.component.id

    def add_empty_answer(self, **kwargs):
        question = kwargs.pop("question", None)
        test_unique = kwargs.pop("test_unique", None)

        # cevabı soru parçası istatistiklerine ekleyelim
        ComponentAnswerStat.objects.create(
            component=self.component,
            question=question,
            test_unique=test_unique,
            user=self.request.user,
            answer_is_true=0,
            answer_is_empty=1
        )

        return self.component.id
