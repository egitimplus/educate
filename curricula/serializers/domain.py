from rest_framework import serializers
from curricula.models import LearningDomain


class LearningDomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = LearningDomain
        fields = ('id', 'name', 'slug', 'content', 'position', 'created', 'updated')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }

