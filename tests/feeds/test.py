from components.models import ComponentAnswerStat, ComponentStat
from questions.models import QuestionAnswerStat


class TestRepository:

    def __init__(self, request, **kwargs):
        self.request = request
