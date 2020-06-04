from companies.models import Lesson
from rest_framework import serializers


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'slug', 'curricula', 'school')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }







