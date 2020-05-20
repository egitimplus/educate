from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


class SchoolLessonTeacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    duration = models.PositiveSmallIntegerField()
    teacher = models.ForeignKey('companies.SchoolTeacher', on_delete=models.CASCADE)
    lesson = models.ForeignKey('companies.Lesson', on_delete=models.CASCADE)
    publisher = models.ForeignKey('publishers.Publisher', on_delete=models.CASCADE)
    pattern = GenericRelation('users.Pattern')

    class Meta:
        db_table = 'companies_school_lesson_teacher'
        default_permissions = ()
        permissions = (
            ("list_school_lesson_teachers", "List school lesson teachers"),  # SchoolViewSet@lesson_teacher_list
            ("filter_school_lesson_teachers", "List school lesson teachers"), # SchoolViewSet@lesson_teacher_filter_list
        )

    def __str__(self):
        return self.name
