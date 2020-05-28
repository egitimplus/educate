from rest_framework import permissions
from companies.models import School
from companies.feeds import SchoolRepository


class ClassroomSchoolObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        school = School.objects.get(id=obj.school_id)

        sr = SchoolRepository(school=school)

        group_manager = sr.group_manager_id()
        if group_manager == request.user.id:
            return True

        school_managers = sr.manager_ids()
        if request.user.id in school_managers:
            return True

        return False


