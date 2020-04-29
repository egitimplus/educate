from rest_framework import serializers
from components.models import Component, ComponentStat
from . import ComponentStatSerializer


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', 'name', 'level', 'active', 'group', 'seconds', 'file')


class ComponentUserSerializer(serializers.ModelSerializer):

    stat = serializers.SerializerMethodField()

    class Meta:
        model = Component
        fields = ('id', 'name', 'level', 'active', 'group', 'seconds', 'file', 'stat')

    def get_stat(self, component):

        request = self.context.get("request")
        queryset = ComponentStat.objects.filter(component=component, user_id=request.user.id).first()
        serializer = ComponentStatSerializer(queryset, many=False)

        return serializer.data
