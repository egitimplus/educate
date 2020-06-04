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
            ("list_schools", "List school"),  # SchoolViewSet@list
            ("view_school", "View school"),  # SchoolViewSet@retrieve
            ("add_school", "Add school"),  # SchoolViewSet@create
            ("change_school", "Update school"),  # SchoolViewSet@update
            ("update_school", "Update school"),  # SchoolViewSet@update_school
            ("delete_school", "Delete school"),  # SchoolViewSet@destroy
            ("list_school_classrooms", "View school classroom list"),  # SchoolViewSet@classroom_list
            ("list_school_lessons", "List school lessons"),  # SchoolViewSet@lesson_list
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

    def __str__(self):
        return self.name
