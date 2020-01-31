from django.db import models


class ClassroomTeacher(models.Model):
    teacher = models.ForeignKey('users.User', on_delete=models.CASCADE)
    classroom = models.ForeignKey('companies.Classroom', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies_classroom_teacher'