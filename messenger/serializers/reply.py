from rest_framework import serializers
from messenger.models import Reply


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id', 'status', 'trashed', 'description', 'file', 'user', 'solver', 'thread', 'lesson', 'created',
                  'updated')
