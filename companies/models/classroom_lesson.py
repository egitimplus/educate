from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


class ClassroomLesson(models.Model):
    lesson = models.ForeignKey('companies.SchoolLessonTeacher', on_delete=models.CASCADE)
    classroom = models.ForeignKey('companies.Classroom', on_delete=models.CASCADE)

    pattern = GenericRelation('users.Pattern')

    class Meta:
        db_table = 'companies_classroom_lesson'
        default_permissions = ()
        permissions = (
            ("add_classroom_lesson", "Attach Lesson to Classroom "), # ClassroomViewSet@attach_lesson
            ("delete_classroom_lesson", "Detach Lesson From Classroom"), # ClassroomViewSet@detach_lesson
            ("change_classroom_lesson", "Change Classroom Lesson"), # ClassroomViewSet@
            ("view_classroom_lesson", "View Classroom Lesson"), # ClassroomViewSet@
            ("list_classroom_lessons", "List Classroom Lesson") # ClassroomViewSet@
        )

    def __str__(self):
        return self.lesson.name
