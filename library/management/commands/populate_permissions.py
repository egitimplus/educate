from django.core.management.base import BaseCommand
from library.models import *


class Command(BaseCommand):

    def _data_crate(self):

        BackendPerms.objects.bulk_create([
            BackendPerms(view_name='ClassroomViewSet', view_action='list', permission_name='companies.list_classrooms'),
            BackendPerms(view_name='ClassroomViewSet', view_action='create', permission_name='companies.add_classroom'),
            BackendPerms(view_name='ClassroomViewSet', view_action='retrieve', permission_name='companies.view_classroom'),
            BackendPerms(view_name='ClassroomViewSet', view_action='destroy', permission_name='companies.delete_classroom'),
            BackendPerms(view_name='ClassroomViewSet', view_action='update', permission_name='companies.change_classroom'),
            BackendPerms(view_name='ClassroomViewSet', view_action='student_list', permission_name='companies.list_classroom_students'),
            BackendPerms(view_name='ClassroomViewSet', view_action='attach_student', permission_name='companies.add_classroom_student'),
            BackendPerms(view_name='ClassroomViewSet', view_action='detach_student', permission_name='companies.remove_classroom_student'),
            BackendPerms(view_name='ClassroomViewSet', view_action='teacher_list', permission_name='companies.list_classroom_teachers'),
            BackendPerms(view_name='ClassroomViewSet', view_action='attach_teacher', permission_name='companies.add_classroom_teacher'),
            BackendPerms(view_name='ClassroomViewSet', view_action='detach_teacher', permission_name='companies.remove_classroom_teacher'),
            BackendPerms(view_name='ClassroomViewSet', view_action='lesson_list', permission_name='companies.list_classroom_lessons'),
            BackendPerms(view_name='ClassroomViewSet', view_action='attach_lesson', permission_name='companies.add_classroom_lesson'),
            BackendPerms(view_name='ClassroomViewSet', view_action='detach_lesson', permission_name='companies.delete_classroom_lesson'),
            BackendPerms(view_name='CompanyGroupViewSet', view_action='list', permission_name='companies.list_companygroups'),
            BackendPerms(view_name='CompanyGroupViewSet', view_action='create', permission_name='companies.add_companygroup'),
            BackendPerms(view_name='CompanyGroupViewSet', view_action='retrieve', permission_name='companies.view_companygroup'),
            BackendPerms(view_name='CompanyGroupViewSet', view_action='destroy', permission_name='companies.delete_companygroup'),
            BackendPerms(view_name='CompanyGroupViewSet', view_action='update', permission_name='companies.change_companygroup'),
            BackendPerms(view_name='CompanyGroupViewSet', view_action='school_list', permission_name='companies.list_companygroup_schools'),
            BackendPerms(view_name='CompanyGroupViewSet', view_action='publisher_list', permission_name='companies.list_companygroup_publishers'),
            BackendPerms(view_name='SchoolViewSet', view_action='list', permission_name='companies.list_school'),
            BackendPerms(view_name='SchoolViewSet', view_action='create', permission_name='companies.add_school'),
            BackendPerms(view_name='SchoolViewSet', view_action='retrieve', permission_name='companies.view_school'),
            BackendPerms(view_name='SchoolViewSet', view_action='destroy', permission_name='companies.delete_school'),
            BackendPerms(view_name='SchoolViewSet', view_action='update', permission_name='companies.change_school'),
            BackendPerms(view_name='SchoolViewSet', view_action='student_list', permission_name='companies.list_school_students'),
            BackendPerms(view_name='SchoolViewSet', view_action='attach_student', permission_name='companies.add_school_student'),
            BackendPerms(view_name='SchoolViewSet', view_action='detach_student', permission_name='companies.delete_school_student'),
            BackendPerms(view_name='SchoolViewSet', view_action='teacher_list', permission_name='companies.list_school_teachers'),
            BackendPerms(view_name='SchoolViewSet', view_action='attach_teacher', permission_name='companies.add_school_teacher'),
            BackendPerms(view_name='SchoolViewSet', view_action='detach_teacher', permission_name='companies.delete_school_teacher'),
            BackendPerms(view_name='SchoolViewSet', view_action='manager_list', permission_name='companies.list_school_managers'),
            BackendPerms(view_name='SchoolViewSet', view_action='attach_manager', permission_name='companies.add_school_manager'),
            BackendPerms(view_name='SchoolViewSet', view_action='detach_manager', permission_name='companies.delete_school_manager'),
            BackendPerms(view_name='SchoolViewSet', view_action='user_list', permission_name='companies.list_school_users'),
            BackendPerms(view_name='SchoolViewSet', view_action='attach_user', permission_name='companies.add_school_user'),
            BackendPerms(view_name='SchoolViewSet', view_action='detach_user', permission_name='companies.delete_school_user'),
            BackendPerms(view_name='SchoolViewSet', view_action='lesson_teacher_filter_list', permission_name='companies.list_school_lessons'),
            BackendPerms(view_name='SchoolViewSet', view_action='lesson_teacher_list', permission_name='companies.list_school_lessons'),
            BackendPerms(view_name='SchoolViewSet', view_action='attach_lesson_teacher', permission_name='companies.add_school_lesson'),
            BackendPerms(view_name='SchoolViewSet', view_action='detach_lesson_teacher', permission_name='companies.delete_school_lesson'),
            BackendPerms(view_name='SchoolViewSet', view_action='lesson_list', permission_name='companies.list_school_lessons'),
            BackendPerms(view_name='SchoolViewSet', view_action='classroom_list', permission_name='companies.list_school_classrooms'),

        ])


    def handle(self, *args, **options):
        self._data_crate()
