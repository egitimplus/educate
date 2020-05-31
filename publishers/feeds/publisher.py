from companies.feeds import CompanyRepository


class PublisherRepository(CompanyRepository):

    def __init__(self, **kwargs):
        self.__object = kwargs.pop("publisher", None)

