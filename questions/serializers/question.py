from rest_framework import serializers
from questions.models import Question
from educategories.serializers import EduCategorySimpleSerializer
from publishers.serializers import SourceQuestionSerializer
from questions.serializers import QuestionAnswerPostSerializer


class QuestionSerializer(serializers.ModelSerializer):

    source_questions = SourceQuestionSerializer(many=True)
    answers = QuestionAnswerPostSerializer(many=True)
    edu_category = EduCategorySimpleSerializer(many=False)

    class Meta:
        model = Question
        fields = ('id', 'name', 'level', 'question_start_type', 'question_start_value', 'question_answer_type',
                  'question_answer_value', 'question_pattern', 'answers', 'active', 'seconds',
                  'source_questions', 'edu_category')










