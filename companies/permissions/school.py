from rest_framework.permissions import IsAuthenticated, IsAdminUser
from library.feeds import GlobalPermissions
from .object_permissions import SchoolObjectPermission

class SchoolPermissionMixin(object):

    def get_permissions(self):

        school_object_permission_list = ['create', 'retrieve', 'destroy', 'update', 'student_list', 'attach_student',
                                         'detach_student', 'teacher_list', 'attach_teacher', 'detach_teacher',
                                         'manager_list', 'attach_teacher', 'detach_teacher', 'user_list', 'attach_user',
                                         'detach_user', 'lesson_list', 'lesson_teacher_filter_list', 'classroom_list',
                                         'lesson_teacher_list', 'attach_lesson_teacher', 'detach_lesson_teacher']
        admin_permission_list = ['list']

        if self.action in school_object_permission_list:

            permission_classes = [
                IsAuthenticated,
                GlobalPermissions,
                SchoolObjectPermission
            ]
        elif self.action in admin_permission_list:

            permission_classes = [
                IsAdminUser,
                GlobalPermissions
            ]
        else:
            permission_classes = [
                IsAuthenticated,
                GlobalPermissions
            ]
        permission_classes = []
        return [permission() for permission in permission_classes]


