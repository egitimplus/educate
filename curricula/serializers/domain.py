from rest_framework import serializers
from curricula.models import LearningDomain
from .test import LearningTestSerializer


class LearningDomainSerializer(serializers.ModelSerializer):

    test = LearningTestSerializer(many=True, required=False)

    class Meta:
        model = LearningDomain
        fields = ('id', 'name', 'slug', 'content', 'position', 'test', 'created', 'updated')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }

    def create(self, validated_data):
        domain = LearningDomain.objects.create(**validated_data)

        return domain

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.content = validated_data['content']
        instance.position = validated_data['position']
        instance.save()
        return instance
