from companies.models import CompanyGroup


class CompanyRepository:

    def __init__(self, request, **kwargs):
        self.request = request

    def school_group_manager_id(self, group_id):
        group = CompanyGroup.objects.filter(id=group_id).first()
        if not group:
            return 0
        return group.user_id

    def school_manager_ids(self, school):
        return school.manager.all().values_list('id', flat=True)

    def classroom_teacher_ids(self, classroom):
        return classroom.teacher.all().values_list('id', flat=True)

