from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class SchoolUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'identity_number')
