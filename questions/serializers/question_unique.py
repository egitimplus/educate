from rest_framework import serializers
from questions.models import QuestionUnique


class QuestionUniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionUnique
        fields = ('id', 'question_code', 'created', 'updated')
