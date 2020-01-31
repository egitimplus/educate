from rest_framework import serializers
from messenger.models import ReplyAnswer


class ReplyAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyAnswer
        fields = ('id', 'description', 'type', 'file', 'user', 'reply', 'created', 'updated')
