from companies.models import Lesson, School
from rest_framework import serializers
from curricula.models import LearningLesson


class LessonSerializer(serializers.ModelSerializer):

    curricula_id = serializers.IntegerField()
    school_id = serializers.IntegerField(required=False)

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'slug', 'curricula_id', 'school_id')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }

    def validate_curricula_id(self, value):
        curricula = LearningLesson.objects.filter(id=value).exists()

        if not curricula:
            raise serializers.ValidationError('Seçilen müfredat bulunamadı.')

        return value

    def validate_school_id(self, value):
        school = School.objects.filter(id=value).exists()

        if not school:
            raise serializers.ValidationError('Seçilen okul bulunamadı.')

        return value

    def create(self, validated_data):
        lesson = Lesson.objects.create(**validated_data)

        return lesson

    def update(self, instance, validated_data):

        instance.name = validated_data['name']
        instance.curricula_id = validated_data['curricula_id']
        instance.save()

        return instance




