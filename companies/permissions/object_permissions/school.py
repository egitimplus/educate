from rest_framework import permissions
from companies.feeds import SchoolRepository


class SchoolObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        sr = SchoolRepository(school=obj)

        if sr.group_manager == request.user:
            return True

        if request.user.id in sr.managers.values_list('id', flat=True):
            return True

        return False
