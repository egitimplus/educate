from questions.models import QuestionUniqueStat
from library.mixins import TestUniqueMixin, RequestMixin


class QuestionUniqueRepository(TestUniqueMixin, RequestMixin):

    def __init__(self, **kwargs):
        self.__question = kwargs.pop("question", None)
        self.__object = kwargs.pop("question_unique", None)
        self.__test_unique = self.__question.test_unique
        self.__request = self.__question.request
        self.__answer_is_true = 0

    def update_stats(self):
        # unique soru istatistiklerini ekleyelim
        QuestionUniqueStat.objects.update_or_create(
            question_unique_id=self.__object.id,
            user=self.__request.user,
            defaults=self.status()
        )

    def status(self):

        question_unique_stat = QuestionUniqueStat.objects.filter(id=self.__object.id).first()

        true_question_diff = 10
        false_question_diff = 20
        true_question_percent = 50

        repeat = 0
        percent = 0
        solved = 1

        if question_unique_stat:
            repeat = question_unique_stat.repeat
            percent = question_unique_stat.percent
            solved = question_unique_stat.solved + 1

        if self._answer_is_true == 1:
            repeat = repeat + 1 if repeat > 0 else 1
            percent = percent + true_question_diff if percent > 40 else 50
        else:
            repeat = repeat - 1 if repeat < 0 else -1
            percent = percent - (repeat * false_question_diff)
            if percent < 0:
                percent = 0

        status = 1 if percent >= true_question_percent else 0

        return {
            'status': status,
            'percent': percent,
            'solved': solved,
            'repeat': repeat
        }

    @property
    def answer_is_true(self):
        return self.__answer_is_true

    @answer_is_true.setter
    def answer_is_true(self, value):
        self.__answer_is_true = value

