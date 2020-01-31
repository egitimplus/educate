from django.db import models


class LearningTestUnique(models.Model):
    id = models.AutoField(primary_key=True)
    learning_test = models.ForeignKey('curricula.LearningTest', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='learning_test_user', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'curricula_learning_test_unique'
        default_permissions = ()
        permissions = (
            ("view_learningtestunique", "View learning test unique"),
            ("list_learningtestunique", "List learning test unique")
        )
