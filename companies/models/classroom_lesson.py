from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


class ClassroomLesson(models.Model):
    lesson = models.ForeignKey('companies.SchoolLessonTeacher', on_delete=models.CASCADE)
    classroom = models.ForeignKey('companies.Classroom', on_delete=models.CASCADE)

    pattern = GenericRelation('users.Pattern')

    class Meta:
        db_table = 'companies_classroom_lesson'
