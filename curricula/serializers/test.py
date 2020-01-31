from curricula.models import LearningTest
from rest_framework import serializers


class LearningTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningTest
        fields = ('id', 'name')

