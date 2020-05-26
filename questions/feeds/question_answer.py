from components.feeds import ComponentMixin
from questions.models import QuestionAnswerStat
from library.mixins import TestUniqueMixin, RequestMixin


class QuestionAnswerRepository(TestUniqueMixin, RequestMixin, ComponentMixin):
    _answer_count = 1

    def __init__(self, **kwargs):
        self._question = kwargs.pop("question", None)
        self._answer = kwargs.pop("question_answer", None)

    def add_answer(self):
        # cevabı soru istatistiklerine ekleyelim
        QuestionAnswerStat.objects.create(
            answer_is_true=self.answer_is_true(),
            answer_seconds=0,
            answer_type=1,
            question=self._question.queryset,
            user=self._request.user,
            test_unique=self._test_unique,
            question_answer_id=self._answer.id,
            answer_count=self._answer_count
        )

    def answer_is_true(self):
        if self._answer.id == self._question.true_answer.id:
            return 1

        return 0

    @property
    def answer_count(self):
        return self._answer_count

    @answer_count.setter
    def answer_count(self, value):
        self._answer_count = value




