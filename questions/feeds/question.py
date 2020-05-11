from questions.models import QuestionAnswerStat
import math


class QuestionRepository:

    def __init__(self, request, **kwargs):
        self.request = request

    """
    " Puan Hesaplama Kuralları
    " -------------------------------------
    " 
    "
    "
    """
    def question_unique_status(self, question_unique_stat, answer_is_true):

        true_question_diff = 10
        false_question_diff = 20
        true_question_percent = 50

        repeat = question_unique_stat.repeat
        percent = question_unique_stat.percent

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
            'solved': question_unique_stat.solved + 1,
            'repeat': repeat
        }

    def components(self):
        pass

    def sub_components(self):
        pass
