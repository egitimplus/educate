from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from users.feeds import create_activate_token
import datetime

User = get_user_model()


class UserUpdateSerializer(serializers.ModelSerializer):

    city = serializers.IntegerField(required=True)
    birth_date = serializers.DateField(required=True)
    phone = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'city', 'birth_date', 'phone')

    def validate_birth_date(self, value):

        if not value:
            raise serializers.ValidationError("Doğum tarihi boş olamaz.")

        if isinstance(value, datetime.date):
            return value

        return datetime.datetime.strptime(value, '%d.%m.%Y')
