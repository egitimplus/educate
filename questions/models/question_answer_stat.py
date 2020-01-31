from django.db import models


class QuestionAnswerStat(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey('questions.Question', related_name='question_answer_stat_question', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='question_answer_stat_user', on_delete=models.CASCADE)
    test_unique = models.ForeignKey('tests.TestUnique', related_name='question_answer_stat_test_unique', on_delete=models.CASCADE)
    question_answer = models.ForeignKey('questions.QuestionAnswer', related_name='question_answer_stat_question_answer', on_delete=models.CASCADE)
    answer_is_true = models.SmallIntegerField()
    answer_seconds = models.SmallIntegerField()
    answer_type = models.SmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'questions_question_answer_stat'
        default_permissions = ()
        permissions = (
            ("view_questionanswerstat", "View question answer stat"),
            ("list_questionanswerstat", "List question answer stat")
        )
