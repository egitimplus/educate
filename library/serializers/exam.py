from rest_framework import serializers
from library.models.exam import Exam


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'name')
