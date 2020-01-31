from rest_framework import serializers
from companies.models import ClassroomLesson


class ClassLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomLesson
        fields = ('lesson', 'classroom')