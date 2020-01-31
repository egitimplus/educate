from rest_framework import serializers
from tests.models import Test
from questions.serializers import QuestionSerializer
from educategories.serializers import EduCategorySimpleSerializer


class TestSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(read_only=True, many=True)
    categories = EduCategorySimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Test
        fields = ('id', 'name', 'test_seconds', 'questions', 'test_type_id', 'publisher', 'test_start', 'categories',
                  'created', 'updated')


