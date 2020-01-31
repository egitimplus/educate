from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from users.feeds import create_activate_token
from datetime import datetime

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    school_id = serializers.IntegerField(required=False)
    identity_number = serializers.CharField(required=True)
    country = serializers.IntegerField(required=False)
    city = serializers.IntegerField(required=False)
    birth_date = serializers.DateField(required=False)
    phone = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', 'identity_number',
                  'country', 'city', 'birth_date', 'phone', 'school_id')

        extra_kwargs = {
            "password": {"write_only": True},
            "password_check": {"write_only": True},
        }

    def validate_email(self, value):
        email = User.objects.filter(email=value).exists()
        if not email:
            return value

        raise serializers.ValidationError("Email daha önce kayıt edilmiş.")

    def validate_identity_number(self, value):
        identify_id = User.objects.filter(identity_number=value).exists()

        if not identify_id:
            return value

        raise serializers.ValidationError("Tc no daha önce kayıt edilmiş.")

    def validate_birth_date(self, value):

        return datetime.strptime(value, '%d.%m.%Y')


    def create(self, validated_data):

        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)

        user.set_password(password)
        # user.is_active = 1

        new_token = create_activate_token()
        user.is_active = 0
        user.register_email_activate_token = new_token
        send_mail(
            'Educate Hoşgeldiniz',
            'Aramıza hoş geldiniz. Üyelik aktifleştirme kodunuz : ' + str(new_token) + ' \\r\\n Üyeliğinizi aktifleştirmek için <a href=\'http://127.0.0.1:1881/\'>tıklayın.</a>',
            'noreply@educate.com.tr',
            [user.email],
            fail_silently=True,
        )


        user.save()
        return user
