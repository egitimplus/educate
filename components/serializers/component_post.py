from rest_framework import serializers
from components.models import Component
from educategories.models import EduCategory


class ComponentPostSerializer(serializers.ModelSerializer):

    edu_category_id = serializers.IntegerField(required=False)
    sub_components = serializers.ListField(
        default=[],
        required=False,
        child=serializers.IntegerField()
    )

    class Meta:
        model = Component
        fields = ('id', 'name', 'edu_category_id', 'level', 'group', 'active', 'sub_components')
        extra_kwargs = {
            'name': {'required': True},
            'level': {'required': False},
            'group': {'required': False},
            'active': {'required': False},
        }

    def validate_edu_category_id(self, value):

        # kategoriler veritabanında kayıtlı mı kontrolü
        edu_category = EduCategory.objects.filter(id=value).exists()

        if not edu_category:
            raise serializers.ValidationError('Seçilen bazı kategoriler bulunamadı.')

        return value

    def create(self, validated_data):
        sub_components = validated_data.pop('sub_components', None)
        component = Component.objects.create(**validated_data)

        return component

    def update(self, instance, validated_data):

        sub_components = validated_data.pop('sub_components', None)

        instance.name = validated_data['name']
        instance.level = validated_data['level']
        instance.active = validated_data['active']
        instance.save()

        instance.to_component.clear()
        if sub_components:
            for sub_component in sub_components:
                instance.to_component.add(sub_component)

        return instance
