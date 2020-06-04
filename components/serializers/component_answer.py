from rest_framework import serializers
from components.models import ComponentAnswer


class ComponentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentAnswer
        fields = ('id', 'component', 'component_ok')
