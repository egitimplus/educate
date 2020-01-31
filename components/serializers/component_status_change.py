from rest_framework import serializers
from components.models import ComponentStatusChange


class ComponentStatusChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentStatusChange
        fields = ('id', 'old_status', 'new_status', 'component', 'user', 'created', 'updated')
