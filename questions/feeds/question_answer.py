from components.feeds import ComponentMixin


class QuestionAnswerRepository(ComponentMixin):

    def __init__(self, request, question_answer):
        self.request = request
        self.queryset = question_answer
