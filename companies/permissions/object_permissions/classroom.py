from rest_framework import permissions
from companies.feeds import SchoolRepository, ClassroomRepository
from companies.models import School


class ClassroomObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        school = School.objects.get(id=obj.school_id)

        sr = SchoolRepository(school=school)

        if sr.group_manager == request.user:
            return True

        if request.user.id in sr.managers.values_list('id', flat=True):
            return True

        cr = ClassroomRepository(classroom=obj)
        cr.request = request

        if request.user.id in cr.teachers.values_list('id', flat=True):
            return True

        return False
