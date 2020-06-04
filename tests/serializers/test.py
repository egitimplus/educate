from rest_framework import serializers
from tests.models import Test
from questions.serializers import QuestionSerializer
from educategories.serializers import EduCategorySerializer
from publishers.serializers import PublisherSerializer


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ('id', 'name', 'test_seconds', 'test_type_id', 'test_start', 'created', 'updated')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.context.get('simple'):
            self.fields['question_count'] = serializers.SerializerMethodField()
        else:
            self.fields['publisher'] = PublisherSerializer(read_only=True, many=True)
            self.fields['questions'] = QuestionSerializer(read_only=True, many=True)
            self.fields['categories'] = EduCategorySerializer(read_only=True, many=True)

    def get_question_count(self, instance):

        return instance.questions.count()
