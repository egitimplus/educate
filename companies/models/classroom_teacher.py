from django.db import models


class ClassroomTeacher(models.Model):
    teacher = models.ForeignKey('users.User', on_delete=models.CASCADE)
    classroom = models.ForeignKey('companies.Classroom', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies_classroom_teacher'
        default_permissions = ()
        permissions = (
            ("list_classroom_teachers", "List Classroom Teachers"), # ClassroomViewSet@teacher_list
            ("add_classroom_teacher", 'Attach Teacher to Classroom'), # ClassroomViewSet@attach_teacher
            ("delete_classroom_teacher", 'Detach Teacher From Classroom'), # ClassroomViewSet@detach_teacher
            ("view_classroom_teacher", "View Classroom Teacher"),  # ClassroomViewSet@
        )