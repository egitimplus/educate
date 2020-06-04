from companies.models import SchoolLessonTeacher
from rest_framework import serializers


class SchoolLessonTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolLessonTeacher
        fields = ('id', 'name', 'duration', 'lesson', 'teacher', 'publisher')
        extra_kwargs = {
            'lesson': {'required': False},
        }
