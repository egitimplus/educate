class CompanyRepository:

    def __init__(self, request, company):
        self._request = request
        self._queryset = company
