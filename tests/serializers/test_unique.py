from rest_framework import serializers
from tests.models import TestUnique


class TestUniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestUnique
        fields = ('id', 'report', 'user', 'test', 'created', 'updated', 'test_result')
