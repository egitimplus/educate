from django.db import models


class QuestionUnique(models.Model):
    id = models.AutoField(primary_key=True)
    question_code = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'questions_question_unique'
        default_permissions = ()
        permissions = (
            ("view_questionunique", "View question unique"),
            ("list_questionunique", "List question unique")
        )
