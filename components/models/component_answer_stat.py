from django.db import models


class ComponentAnswerStat(models.Model):
    id = models.AutoField(primary_key=True)
    component = models.ForeignKey('components.Component', related_name='component_answer_stat_component', on_delete=models.CASCADE)
    question = models.ForeignKey('questions.Question', related_name='component_answer_stat_question', on_delete=models.CASCADE)
    test_unique = models.ForeignKey('tests.TestUnique', related_name='component_answer_stat_test_unique', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='component_answer_stat_user', on_delete=models.CASCADE)
    answer_is_true = models.SmallIntegerField()
    answer_is_empty = models.SmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'components_component_answer_stat'
        default_permissions = ()
        permissions = (
            ("view_componentanswerstat", "View component answer stat"),
            ("list_componentanswerstat", "List component answer stat")
        )