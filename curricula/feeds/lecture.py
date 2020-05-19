from components.feeds import ComponentMixin


class LectureRepository(ComponentMixin):

    def __init__(self, request, lecture):
        self.request = request
        self.queryset = lecture
