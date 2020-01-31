from rest_framework import permissions
from companies.feeds import CompanyRepository


class SchoolObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        company_repo = CompanyRepository(request=request)

        group_manager = company_repo.school_group_manager_id(obj.group_id)
        if group_manager == request.user.id:
            return True

        school_managers = company_repo.school_manager_ids(obj)
        if request.user.id in school_managers:
            return True

        return False
