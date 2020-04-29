from rest_framework import serializers
from components.models import ComponentStat


class ComponentStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentStat
        fields = ('id', 'component_status', 'component', 'user', 'created', 'updated')
