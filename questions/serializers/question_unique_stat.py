from rest_framework import serializers
from questions.models import QuestionUniqueStat


class QuestionUniqueStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionUniqueStat
        fields = ('id', 'question_unique', 'status', 'answers', 'user', 'created', 'updated')


