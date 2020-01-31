from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


User = get_user_model()


class LostPasswordChangeSerializer(serializers.Serializer):

    code = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def validate(self, attrs):
        """
        Check that the start is before the stop.
        """
        user = User.objects.filter(password_reset_token=attrs['code'], email=attrs['email']).exists()

        if not user:
            raise serializers.ValidationError("Kayıt bulunamadı.")
        return attrs
