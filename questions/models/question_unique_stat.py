from django.db import models


class QuestionUniqueStat(models.Model):
    id = models.AutoField(primary_key=True)
    question_unique = models.ForeignKey('questions.QuestionUnique', related_name='question_unique_stat_question_unique', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='question_unique_stat_user', on_delete=models.CASCADE)
    question_code = models.CharField(max_length=255)
    status = models.SmallIntegerField()
    answers = models.TextField(default='[]')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    percent = models.SmallIntegerField()
    solved = models.SmallIntegerField()
    repeat = models.SmallIntegerField()

    class Meta:
        db_table = 'questions_question_unique_stat'
        default_permissions = ()
        permissions = (
            ("view_questionuniquestat", "View question unique stat"),
            ("list_questionuniquestat", "List question unique stat")
        )

