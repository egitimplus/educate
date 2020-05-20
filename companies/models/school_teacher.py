from django.db import models


class SchoolTeacher(models.Model):
    teacher = models.ForeignKey('users.User', on_delete=models.CASCADE)
    school = models.ForeignKey('companies.School', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies_school_teacher'
        default_permissions = ()
        permissions = (
            ("add_school_teacher", 'Attach teacher to school'),  # SchoolViewSet@attach_teacher
            ("delete_school_teacher", 'Detach teacher from school'),  # SchoolViewSet@detach_teacher
            ("list_school_teachers", "List school teachers"),  # SchoolViewSet@teacher_list
        )
