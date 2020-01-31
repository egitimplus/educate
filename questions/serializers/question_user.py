from rest_framework import serializers
from questions.models import Question
from educategories.serializers import EduCategorySerializer
from components.serializers import ComponentSerializer
from .question_answer import QuestionAnswerSerializer


class QuestionUserSerializer(serializers.ModelSerializer):

    edu_category = EduCategorySerializer(many=False)
    component = ComponentSerializer(many=True)
    question_answers = QuestionAnswerSerializer(many=True)
    level = serializers.CharField(source='get_level_display')

    #question_answer_type = serializers.CharField(source='get_question_answer_type_display')
    #question_start_type = serializers.CharField(source='get_question_start_type_display')

    class Meta:
        model = Question
        fields = ('id', 'name', 'level', 'question_start_type', 'question_start_value', 'question_answer_type',
                  'question_answer_value', 'question_pattern', 'active', 'created', 'updated', 'edu_category',
                  'component', 'question_answers')
