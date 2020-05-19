class CompanyRepository:

    def __init__(self, request, company):
        self.request = request
        self.queryset = company
