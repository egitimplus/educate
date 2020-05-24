from components.feeds import ComponentStatRepository
from questions.models import QuestionAnswerStat
from questions.models import QuestionUnique, QuestionUniqueStat


class QuestionUniqueRepository:

    def __init__(self, request, **kwargs):
        self.request = request
        self.question = kwargs.pop("question", None)
        self.queryset = kwargs.pop("question_unique", None)
        self.test_unique = kwargs.pop("test_unique", None)

    def update_stats(self, answer_is_true):

        question_unique_stat = QuestionUniqueStat.objects.filter(id=self.queryset.id).first()

        # verilen cevaba göre soru için yeni bir kod oluşturalım
        question_unique = self.status(question_unique_stat, answer_is_true)

        # unique soru istatistiklerini ekleyelim
        QuestionUniqueStat.objects.update_or_create(
            question_unique_id=self.queryset.id,
            user=self.request.user,
            defaults={
                "status": question_unique['status'],
                "percent": question_unique['percent'],
                "solved": question_unique['solved'],
                "repeat": question_unique['repeat'],
            }
        )

    def status(self, question_unique_stat, answer_is_true):

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

        if answer_is_true == 1:
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



