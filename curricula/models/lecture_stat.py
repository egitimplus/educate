from django.db import models


class LearningLectureStat(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', related_name='lecture_stat_user', on_delete=models.CASCADE)
    lecture = models.ForeignKey('curricula.LearningLecture', related_name='lecture_stat', on_delete=models.CASCADE)
    lecture_status = models.PositiveSmallIntegerField(default=0)
    practice_status = models.PositiveSmallIntegerField(default=0)
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'curricula_learning_lecture_stat'
        default_permissions = ()
        permissions = (
            ("view_learninglecturestat", "View learning lecture stat"),
            ("list_learninglecturestat", "List learning lecture stat")
        )