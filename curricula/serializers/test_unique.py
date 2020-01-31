from curricula.models import LearningTestUnique
from rest_framework import serializers


class LearningTestUniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningTestUnique
        fields = ('id', 'name')
