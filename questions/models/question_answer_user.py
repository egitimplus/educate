from django.db import models


class UserQuestionAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', related_name='user_question_answer_user', on_delete=models.CASCADE)
    question = models.ForeignKey('questions.Question', related_name='user_question_answer_question', on_delete=models.CASCADE)
    source = models.ForeignKey('publishers.Source', related_name='user_question_answer_source', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    answer = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    check = models.SmallIntegerField()

    class Meta:
        db_table = 'questions_user_question_answers'
        default_permissions = ()
        permissions = (
            ("view_userquestionanswer", "View user question answer"),
            ("list_userquestionanswer", "List user question answer")
        )