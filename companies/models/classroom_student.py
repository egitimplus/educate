from django.db import models


class ClassroomStudent(models.Model):
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    classroom = models.ForeignKey('companies.Classroom', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies_classroom_student'
        default_permissions = ()
        permissions = (
            ("list_classroom_students", "List Classroom Students"), # ClassroomViewSet@student_list
            ("add_classroom_student", 'Attach Student to Classroom'), # ClassroomViewSet@attach_student
            ("delete_classroom_student", 'Detach Student From Classroom'), # ClassroomViewSet@detach_student
            ("view_classroom_student", "View Classroom Student"),  # ClassroomViewSet@

        )

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name
