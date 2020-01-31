from django.db import models


class QuestionExam(models.Model):
    question = models.ForeignKey('questions.Question', on_delete=models.CASCADE)
    exam = models.ForeignKey('library.Exam', on_delete=models.CASCADE)
    exam_year = models.SmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'questions_question_exam'
        default_permissions = ()
        permissions = (
            ("view_questionexam", "View question exam"),
            ("list_questionexam", "List question exam")
        )