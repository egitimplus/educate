from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


User = get_user_model()


class PasswordChangeSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_password(self, value):
        validate_password(value)
        return value

