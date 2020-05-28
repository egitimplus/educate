from rest_framework import permissions
from companies.feeds import SchoolRepository


class SchoolObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        sr = SchoolRepository(school=obj)

        group_manager = sr.group_manager_id()
        if group_manager == request.user.id:
            return True

        school_managers = sr.manager_ids()
        if request.user.id in school_managers:
            return True

        return False
