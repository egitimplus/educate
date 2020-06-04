from django.db import models


class ComponentAnswer(models.Model):
    component_ok = models.SmallIntegerField()
    component = models.ForeignKey('components.Component', related_name='component_answers', on_delete=models.CASCADE)
    question_answer = models.ForeignKey('questions.QuestionAnswer',on_delete=models.CASCADE, related_name='answer_components')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'components_component_question_answer'
        default_permissions = ()
        permissions = (
            ("view_componentanswer", "View component answer"),
            ("list_componentanswer", "List component answer")
        )
