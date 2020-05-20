from rest_framework import serializers
from companies.models import *


class ClassLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomLesson
        fields = ('lesson', 'classroom')



