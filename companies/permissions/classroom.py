from library.feeds import GlobalPermissions
from rest_framework.permissions import IsAuthenticated
from .object_permissions import ClassroomSchoolObjectPermission, ClassroomObjectPermission


class ClassroomPermissionMixin(object):

    def get_permissions(self):

        class_object_permission_list = ['retrieve', 'destroy', 'update', 'student_list', 'attach_student',
                                        'detach_student', 'teacher_list', 'attach_teacher', 'detach_teacher',
                                        'lesson_list', 'attach_lesson', 'detach_lesson', 'course', 'course_user',
                                        'course_stat', 'course_lesson', 'course_unit', 'course_lecture_stat']
        school_object_permission_list = ['list', 'create']

        if self.action in class_object_permission_list:

            permission_classes = [
                IsAuthenticated,
                GlobalPermissions,
                ClassroomObjectPermission
            ]
        elif self.action in school_object_permission_list:

            permission_classes = [
                IsAuthenticated,
                GlobalPermissions,
                ClassroomSchoolObjectPermission
            ]

        permission_classes = []
        return [permission() for permission in permission_classes]

