from django.db import models
from django.template.defaultfilters import slugify
import itertools


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    curricula = models.ForeignKey('curricula.LearningLesson', on_delete=models.CASCADE)
    school = models.ForeignKey('companies.School', related_name='lesson_school', on_delete=models.CASCADE)
    lesson_teacher = models.ManyToManyField('companies.SchoolTeacher', through='companies.SchoolLessonTeacher', related_name='school_lesson_teacher')

    class Meta:
        default_permissions = ()
        permissions = (
            ("super_lesson", "All lesson"), # LessonViewSet@all
            ("add_lesson", "Add lesson"), # LessonViewSet@create
            ("change_lesson", "Update lesson"), # LessonViewSet@update
            ("delete_lesson", "Delete lesson"), # LessonViewSet@destroy
            ("list_lessons", "List lesson"), # LessonViewSet@list
            ("view_lesson", "View lesson"), # LessonViewSet@retrieve
            ("attach_lesson_teacher", 'Add lesson teacher'), # LessonViewSet@attach_lesson_teacher
            ("detach_lesson_teacher", 'Detach lesson teacher'), # LessonViewSet@detach_lesson_teacher
            ("update_lesson_teacher", 'Update lesson teacher'), # LessonViewSet@update_lesson_teacher
            ("list_lesson_teacher", 'List lesson teachers') # LessonViewSet@list_lesson_teacher
        )

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not Lesson.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(Lesson, self).save()
