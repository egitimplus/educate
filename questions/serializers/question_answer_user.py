from questions.models import UserQuestionAnswer
from rest_framework import serializers


class UserQuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuestionAnswer
        fields = ('id', 'answer', 'check', 'user', 'question', 'source', 'created', 'updated')
