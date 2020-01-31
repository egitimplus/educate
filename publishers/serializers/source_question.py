from rest_framework import serializers
from publishers.models import Source
from publishers.serializers import QuestionBookSerializer


class SourceQuestionSerializer(serializers.ModelSerializer):

    book = QuestionBookSerializer(many=False)

    class Meta:
        model = Source
        fields = ('id', 'name', 'slug', 'sort_order', 'parent', 'book', 'active', 'created', 'updated')
