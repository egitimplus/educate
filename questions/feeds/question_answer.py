from components.feeds import ComponentMixin
from questions.models import QuestionAnswerStat
from library.mixins import TestUniqueMixin, RequestMixin


class QuestionAnswerRepository(TestUniqueMixin, RequestMixin, ComponentMixin):

    def __init__(self, **kwargs):
        self.__question = kwargs.pop("question", None)
        self.__object = kwargs.pop("question_answer", None)
        self.__test_unique = self.__question.test_unique
        self.__request = self.__question.request
        self.__answer_count = 1

    def add_answer(self):
        # cevabı soru istatistiklerine ekleyelim
        QuestionAnswerStat.objects.create(
            answer_is_true=self.answer_is_true(),
            answer_seconds=0,
            answer_type=1,
            question=self.__question.object,
            user=self.__request.user,
            test_unique=self.__test_unique,
            question_answer_id=self.__object.id,
            answer_count=self.__answer_count
        )

    def answer_is_true(self):
        if self.__object.id == self.__question.true_answer.id:
            return 1

        return 0

    @property
    def answer_count(self):
        return self.__answer_count

    @answer_count.setter
    def answer_count(self, value):
        self.__answer_count = value




