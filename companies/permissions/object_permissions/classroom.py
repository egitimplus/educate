from rest_framework import permissions
from companies.feeds import SchoolRepository, ClassroomRepository
from companies.models import School


class ClassroomObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        school = School.objects.get(id=obj.school_id)

        school_repo = SchoolRepository(request=request, school=school)
        group_manager = school_repo.group_manager_id(school.group_id)

        if group_manager == request.user.id:
            return True

        school_managers = school_repo.manager_ids()
        if request.user.id in school_managers:
            return True

        classroom_repo = ClassroomRepository(request=request, classroom=obj)
        classroom_teachers = classroom_repo.teacher_ids()
        if request.user.id in classroom_teachers:
            return True

        return False
