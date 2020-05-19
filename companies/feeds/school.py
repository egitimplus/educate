from companies.models import CompanyGroup

class SchoolRepository:

    def __init__(self, request, school):
        self.request = request
        self.queryset = school

    def manager_ids(self):
        return self.queryset.manager.all().values_list('id', flat=True)

    def group_manager_id(self):
        group = CompanyGroup.objects.filter(id=self.queryset.group_id).first()
        if not group:
            return 0
        return group.user_id


