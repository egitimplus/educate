from questions.models import QuestionAnswer
from rest_framework import serializers


class QuestionAnswerPostSerializer(serializers.ModelSerializer):

    true_components = serializers.ListField(
        required=False, default=[], child=serializers.IntegerField()
    )

    false_components = serializers.ListField(
        required=False, default=[], child=serializers.IntegerField()
    )

    class Meta:
        model = QuestionAnswer
        fields = ('id', 'answer_type', 'answer_value', 'answer_choice', 'is_true_answer', 'true_components',
                  'false_components')
