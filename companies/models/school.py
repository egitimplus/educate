from django.db import models
from .company import Company
from django.template.defaultfilters import slugify
import itertools
from django.contrib.contenttypes.fields import GenericRelation


class School(Company):
    group = models.ForeignKey('companies.CompanyGroup', related_name='school_group', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    address = models.TextField(default=None, blank=True, null=True)
    code = models.CharField(max_length=255, default=None, blank=True, null=True)

    type = models.ForeignKey('companies.SchoolType', related_name='school_type', on_delete=models.CASCADE)
    teacher = models.ManyToManyField('users.User', through='SchoolTeacher', related_name='school_teachers')
    manager = models.ManyToManyField('users.User', through='SchoolManager', related_name='school_managers')
    student = models.ManyToManyField('users.User', through='SchoolStudent', related_name='school_students')
    user = models.ManyToManyField('users.User', through='SchoolUser', related_name='school_users')
    book = models.ManyToManyField('publishers.Book', through='SchoolBook', related_name='school_books')
    lesson = models.ManyToManyField('curricula.LearningLesson', through='companies.Lesson', related_name='school_curricula')
    test = models.ManyToManyField('tests.Test', through='SchoolTest', related_name='school_tests')

    pattern = GenericRelation('users.Pattern')

    class Meta:
        default_permissions = ()
        permissions = (
            ("super_school", "Super school"),  # SchoolViewSet@all
            ("add_school", "Add school"),  # SchoolViewSet@create
            ("change_school", "Update school"),  # SchoolViewSet@update
            ("update_school", "Update school"),  # SchoolViewSet@update_school
            ("delete_school", "Delete school"),  # SchoolViewSet@destroy
            ("view_school", "View school"),  # SchoolViewSet@retrieve
            ("list_schools", "List school"),  # SchoolViewSet@list
            ("list_school_classrooms", "View school classroom list"),  # SchoolViewSet@classroom_list
            ("list_school_lessons", "List school lessons"),  # SchoolViewSet@lesson_list
            ("list_school_lesson_teachers", "List school lesson teachers"),  # SchoolViewSet@lesson_teacher_list
            ("filter_school_lesson_teachers", "List school lesson teachers"), # SchoolViewSet@lesson_teacher_filter_list
            ("add_school_manager", 'Attach manager to school'),  # SchoolViewSet@attach_manager
            ("delete_school_manager", 'Detach manager from school'),  # SchoolViewSet@detach_manager
            ("list_school_managers","List school managers"),  # SchoolViewSet@manager_list
            ("add_school_student", 'Attach student to school'),  # SchoolViewSet@attach_student
            ("delete_school_student", 'Detach student from school'),  # SchoolViewSet@detach_student
            ("list_school_students", "List school students"),  # SchoolViewSet@student_list
            ("add_school_teacher", 'Attach teacher to school'),  # SchoolViewSet@attach_teacher
            ("delete_school_teacher", 'Detach teacher from school'),  # SchoolViewSet@detach_teacher
            ("list_school_teachers", "List school teachers"),  # SchoolViewSet@teacher_list
            ("add_school_user", 'Attach user to school'), # SchoolViewSet@attach_user
            ("delete_school_user", 'Detach user from school'),  # SchoolViewSet@detach_user
            ("list_school_users", "List school users"),  # SchoolViewSet@user_list
            ("list_school_tests", "List school tests"),  # SchoolViewSet@test_list
            ("update_school_roles", "Update school roles")  # SchoolViewSet@update_roles
        )

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not School.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(School, self).save()


