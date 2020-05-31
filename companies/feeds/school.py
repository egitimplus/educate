from library.mixins import RequestMixin
from companies.feeds import CompanyRepository


class SchoolRepository(CompanyRepository, RequestMixin):

    def __init__(self, **kwargs):
        self.__object = kwargs.pop("school", None)



