from components.feeds import ComponentMixin
from questions.models import QuestionAnswerStat


class QuestionAnswerRepository(ComponentMixin):

    def __init__(self, request, **kwargs):
        test_unique = kwargs.pop("test_unique", None)
        question = kwargs.pop("question", None)

        self._request = request
        self._question = question
        self._test_unique = test_unique
        self._answer_id = None
        self._answer_is_true = None
        self._answer_count = 1

    @property
    def answer_id(self):
        return self._answer_id

    @answer_id.setter
    def answer_id(self, answer_id):
        self._answer_id = answer_id

    @property
    def answer_is_true(self):
        return self._answer_is_true

    @answer_is_true.setter
    def answer_is_true(self, status):
        self._answer_is_true = status

    @property
    def answer_count(self):
        return self._answer_count

    @answer_count.setter
    def answer_count(self, value):
        self._answer_count = value

    def add_answer(self):

        # cevabı soru istatistiklerine ekleyelim
        QuestionAnswerStat.objects.create(
            answer_is_true=self._answer_is_true,
            answer_seconds=0,
            answer_type=1,
            question=self._question,
            user=self._request.user,
            test_unique=self._test_unique,
            question_answer_id=self._answer_id,
            answer_count=self._answer_count
        )


