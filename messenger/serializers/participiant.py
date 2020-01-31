from rest_framework import serializers
from messenger.models.participiant import Participiant


class ParticipiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participiant
        fields = ('id', 'trashed', 'last_read', 'user', 'thread', 'created', 'updated')
