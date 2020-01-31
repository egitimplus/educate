from curricula.models import LearningLesson
from rest_framework import serializers


class LearningLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningLesson
        fields = ('id', 'name', 'slug', 'active', 'public', 'duration', 'created', 'updated')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }

    def create(self, validated_data):
        lesson = LearningLesson.objects.create(**validated_data)

        return lesson

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.active = validated_data['content']
        instance.public = validated_data['position']
        instance.duration = validated_data['duration']
        instance.save()
        return instance
