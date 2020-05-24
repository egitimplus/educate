from components.feeds import ComponentMixin
from questions.models import QuestionAnswerStat


class QuestionAnswerRepository(ComponentMixin):

    def __init__(self, request, **kwargs):
        test_unique = kwargs.pop("test_unique", None)
        question = kwargs.pop("question", None)

        self.request = request
        self.question = question
        self.test_unique = test_unique
        self.answer_id = None
        self.answer_is_true = None
        self.answer_count = 1

    def set_answer_id(self, answer_id):
        self.answer_id = answer_id

    def set_answer_is_true(self, status):
        self.answer_is_true = status

    def set_answer_count(self):
        self.answer_count = self.answer_count + 1

    def add_answer(self):

        # cevabı soru istatistiklerine ekleyelim
        QuestionAnswerStat.objects.create(
            answer_is_true=self.answer_is_true,
            answer_seconds=0,
            answer_type=1,
            question=self.question,
            user=self.request.user,
            test_unique=self.test_unique,
            question_answer_id=self.answer_id,
            answer_count=self.answer_count
        )


