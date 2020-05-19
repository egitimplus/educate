from rest_framework import permissions
from companies.models import School


class ClassroomSchoolObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        company_repo = Sc(request=request)

        school = School.objects.get(id=obj.school_id)

        group_manager = company_repo.school_group_manager_id(school.group_id)
        if group_manager == request.user.id:
            return True

        school_managers = company_repo.school_manager_ids(school)
        if request.user.id in school_managers:
            return True

        return False


