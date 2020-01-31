from django.db import models


class QuestionAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey('questions.Question', related_name='question_answers', on_delete=models.CASCADE)
    answer_type = models.SmallIntegerField()
    answer_value = models.TextField()
    answer_choice = models.SmallIntegerField()
    is_true_answer = models.SmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    component = models.ManyToManyField('components.Component', through='components.ComponentAnswer', related_name='ccc')

    class Meta:
        db_table = 'questions_question_answer'
        default_permissions = ()
        permissions = (
            ("view_questionanswer", "View question answer"),
            ("list_questionanswer", "List question answers")
        )
