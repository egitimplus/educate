from companies.feeds import CompanyRepository


class PublisherRepository(CompanyRepository):

    def __init__(self, **kwargs):
        self._queryset = kwargs.pop("publisher", None)

