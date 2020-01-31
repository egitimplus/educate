from rest_framework import serializers
from messenger.models import Thread


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('id', 'subject', 'user', 'created', 'updated')
