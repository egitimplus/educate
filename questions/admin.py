from django.contrib import admin
from questions.models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionAnswer)
admin.site.register(QuestionAnswerStat)
admin.site.register(QuestionUnique)
admin.site.register(UserQuestionAnswer)
