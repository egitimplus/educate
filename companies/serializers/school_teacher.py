from rest_framework import serializers
from companies.serializers import SchoolUserSerializer
from companies.models import SchoolTeacher


class SchoolTeacherSerializer(serializers.ModelSerializer):

    teacher = SchoolUserSerializer()

    class Meta:
        model = SchoolTeacher
        fields = ('teacher',)
