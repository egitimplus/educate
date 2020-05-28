from rest_framework import permissions
from companies.models import School
from companies.feeds import SchoolRepository


class ClassroomSchoolObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        school = School.objects.get(id=obj.school_id)

        sr = SchoolRepository(school=school)

        if sr.group_manager == request.user:
            return True

        if request.user.id in sr.managers.values_list('id', flat=True):
            return True

        return False


