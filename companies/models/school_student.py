from django.db import models


class SchoolStudent(models.Model):
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    school = models.ForeignKey('companies.School', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies_school_student'
        default_permissions = ()
        permissions = (
            ("add_school_student", 'Attach student to school'),  # SchoolViewSet@attach_student
            ("delete_school_student", 'Detach student from school'),  # SchoolViewSet@detach_student
            ("list_school_students", "List school students"),  # SchoolViewSet@student_list
        )