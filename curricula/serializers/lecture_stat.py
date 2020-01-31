from rest_framework import serializers
from curricula.models import LearningLectureStat


class LearningLectureStatSerializer(serializers.ModelSerializer):
    lecture_id = serializers.IntegerField()

    class Meta:
        model = LearningLectureStat
        fields = ('id', 'lecture_id', 'lecture_status', 'practice_status', 'created')







