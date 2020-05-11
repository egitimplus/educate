from components.models import ComponentAnswerStat, ComponentStat
from questions.models import QuestionAnswerStat


class QuestionStatRepository:

    def __init__(self, request, **kwargs):
        self.request = request

