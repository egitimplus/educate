from rest_framework import permissions
from companies.feeds import SchoolRepository, ClassroomRepository
from companies.models import School


class ClassroomObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        school = School.objects.get(id=obj.school_id)

        sr = SchoolRepository(school=school)
        group_manager = sr.group_manager_id()

        if group_manager == request.user.id:
            return True

        school_managers = sr.manager_ids()
        if request.user.id in school_managers:
            return True

        cr = ClassroomRepository(classroom=obj)
        classroom_teachers = cr.teacher_ids()
        if request.user.id in classroom_teachers:
            return True

        return False
