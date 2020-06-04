from rest_framework import serializers
from curricula.models import LearningLectureStat


class LearningLectureStatSerializer(serializers.ModelSerializer):

    class Meta:
        model = LearningLectureStat
        fields = ('id', 'lecture', 'lecture_status', 'practice_status', 'created')







