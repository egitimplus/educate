from rest_framework import serializers
from components.models import ComponentAnswerStat


class ComponentAnswerStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentAnswerStat
        fields = ('id', 'answer_is_true', 'answer_is_empty', 'component', 'question', 'test_unique', 'user',
                  'created', 'updated')

