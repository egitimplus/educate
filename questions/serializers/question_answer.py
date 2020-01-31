from questions.models import QuestionAnswer
from rest_framework import serializers


class QuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswer
        fields = ('id', 'answer_type', 'answer_value', 'answer_choice', 'is_true_answer')
