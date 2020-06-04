from rest_framework import serializers
from components.models import Component, ComponentStat
from components.serializers import ComponentStatSerializer


class ComponentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Component
        fields = ('id', 'name', 'level', 'active', 'group', 'seconds', 'file')
        extra_kwargs = {
            'name': {'required': True},
            'level': {'required': False},
            'group': {'required': False},
            'active': {'required': False},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('data', False):
            self.fields['sub_components'] = serializers.ListField(
                default=[],
                required=False,
                child=serializers.IntegerField()
            )

            self.fields['edu_category'] = serializers.IntegerField(required=False)
        else:
            request = self.context.get("request")
            stat = self.context.get("stat")

            if request is not None and stat is not None:
                if request.user:
                    self.fields['stat'] = serializers.SerializerMethodField()

    def get_stat(self, component):
        request = self.context.get('request')

        if request is not None:
            if request.user:
                request = self.context.get("request")
                queryset = ComponentStat.objects.filter(component=component, user_id=request.user.id).first()
                serializer = ComponentStatSerializer(queryset, many=False)
                return serializer.data

        return {}

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
