from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


User = get_user_model()


class UserPostSerializer(serializers.ModelSerializer):
    school_id = serializers.IntegerField()
    password_check = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'identity_number',
                  'city', 'birth_date', 'phone', 'school_id', 'password', 'password_check')

    def validate(self, attrs):
        """
        Check that the start is before the stop.
        """
        if attrs['password'] == attrs['password_check']:
            validate_password(attrs['password'])
            return attrs

        raise serializers.ValidationError("Şifreler aynı girilmedi. Lütfen kontrol ediniz.")

    def create(self, validated_data):

        password = validated_data.pop('password', None)
        password_check = validated_data.pop('password_check', None)
        user = User.objects.create(**validated_data)

        user.set_password(password)
        user.is_active = 1
        user.save()

        return user
