from questions.models import QuestionAnswerStat
from rest_framework import serializers


class QuestionAnswerStatSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = QuestionAnswerStat
        fields = ('id', 'answer_is_true', 'answer_seconds', 'answer_type', 'question', 'user', 'test_unique',
                  'question_answer', 'answer_count', 'created', 'updated')
