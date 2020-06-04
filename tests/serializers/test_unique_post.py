from rest_framework import serializers
from tests.models import TestUnique


class TestUniquePostSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = TestUnique
        fields = ('id', 'report', 'user', 'test', 'created', 'updated', 'test_result')

    def create(self, validated_data):

        if 'user' not in validated_data:
            validated_data['user'] = self.context['request'].user

        test_unique = TestUnique.objects.create(**validated_data)

        return test_unique
