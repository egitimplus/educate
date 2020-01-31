from curricula.models import LearningTag
from rest_framework import serializers


class LearningTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningTag
        fields = ('id', 'name', 'slug')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }