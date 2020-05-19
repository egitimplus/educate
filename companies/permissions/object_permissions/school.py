from rest_framework import permissions
from companies.feeds import SchoolRepository


class SchoolObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        school_repo = SchoolRepository(request=request, school=obj)

        group_manager = school_repo.group_manager_id()
        if group_manager == request.user.id:
            return True

        school_managers = school_repo.manager_ids()
        if request.user.id in school_managers:
            return True

        return False
