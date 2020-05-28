from companies.feeds import CompanyRepository


class PublisherRepository(CompanyRepository):

    def __init__(self, **kwargs):
        self._object = kwargs.pop("publisher", None)

