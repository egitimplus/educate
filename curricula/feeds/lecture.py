from components.feeds import ComponentMixin


class LectureRepository(ComponentMixin):

    def __init__(self, request, lecture):
        self._request = request
        self._queryset = lecture
