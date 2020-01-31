from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    school_id = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'identity_number', 'city', 'phone', 'birth_date', 'email', 'school_id')

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)

        if representation['birth_date']:
            representation['birth_date'] = instance.birth_date.strftime('%d.%m.%Y')

        return representation