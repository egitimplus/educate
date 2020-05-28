from library.mixins import RequestMixin


class CompanyRepository(RequestMixin):

    def __init__(self, **kwargs):
        self._queryset = kwargs.pop("company", None)
