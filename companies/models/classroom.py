from django.db import models
from django.template.defaultfilters import slugify
import itertools
from django.contrib.contenttypes.fields import GenericRelation


class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    year = models.PositiveSmallIntegerField()
    grade = models.PositiveSmallIntegerField()
    department_id = models.PositiveSmallIntegerField()
    school = models.ForeignKey('companies.School', on_delete=models.CASCADE)
    active = models.PositiveSmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    student = models.ManyToManyField('users.User', through='companies.ClassroomStudent', related_name='classroom_students')
    teacher = models.ManyToManyField('users.User', through='companies.ClassroomTeacher', related_name='classroom_teachers')
    lesson = models.ManyToManyField('companies.SchoolLessonTeacher', through='companies.ClassroomLesson', related_name='classroom_lessons')

    pattern = GenericRelation('users.Pattern')

    class Meta:
        default_permissions = ()
        permissions = (
            ("super_classroom", "All access for classroom"),  # ClassroomViewSet@all
            ("view_classroom", "View Classroom"), # ClassroomViewSet@retrieve
            ("add_classroom", "Add Classroom"), # ClassroomViewSet@create
            ("change_classroom", "Update Classroom"), # ClassroomViewSet@update
            ("delete_classroom", "Remove Classroom"), # ClassroomViewSet@destroy
            ("list_classrooms", "List Classroom"), # ClassroomViewSet@list
        )

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None):

        if not self.id:

            self.slug = slugify(self.name)
            self.year = '2017'

            for x in itertools.count(1):
                if not Classroom.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(Classroom, self).save()