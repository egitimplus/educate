from rest_framework import serializers
from companies.models import *
from companies.serializers import *


class ClassLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomLesson
        fields = ('lesson', 'classroom')


class NewSchoolLessonTeacherSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = SchoolLessonTeacher
        fields = ('id', 'name', 'publisher','lesson')


class NewClassLessonSerializer(serializers.ModelSerializer):

    lesson = NewSchoolLessonTeacherSerializer()

    class Meta:
        model = ClassroomLesson
        fields = ('lesson', 'classroom')


