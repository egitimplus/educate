class RequestMixin:
    _request = None

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, value):
        self._request = value
