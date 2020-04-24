from django.db import models


class TestQuestion(models.Model):
    question = models.ForeignKey('questions.Question', on_delete=models.CASCADE, related_name='question')
    test = models.ForeignKey('tests.Test', on_delete=models.CASCADE, related_name='test')
    sort_order = models.SmallIntegerField()

    class Meta:
        db_table = 'tests_test_question'
        ordering = ('sort_order',)
