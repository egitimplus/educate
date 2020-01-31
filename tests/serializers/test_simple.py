from rest_framework import serializers
from tests.models import Test


class SimpleTestSerializer(serializers.ModelSerializer):

    question_count = serializers.SerializerMethodField()

    class Meta:
        model = Test
        fields = ('id', 'name', 'question_count')

    def get_question_count(self, instance):

        return instance.questions.count()