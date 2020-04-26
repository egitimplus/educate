from questions.models import QuestionAnswerStat
from rest_framework import serializers


class QuestionAnswerStatPostSerializer(serializers.ModelSerializer):

    question_answer_id = serializers.IntegerField()
    question_id = serializers.IntegerField()
    test_unique_id = serializers.IntegerField()

    class Meta:
        model = QuestionAnswerStat
        fields = ('id', 'answer_is_true', 'answer_seconds', 'answer_type', 'question_id', 'user', 'test_unique_id',
                  'question_answer_id', 'answer_count', 'created', 'updated')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        question_answer_stat = QuestionAnswerStat.objects.create(**validated_data)

        return question_answer_stat
