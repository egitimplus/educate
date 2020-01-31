from rest_framework import serializers
from messenger.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'body', 'user', 'thread', 'created', 'updated')
