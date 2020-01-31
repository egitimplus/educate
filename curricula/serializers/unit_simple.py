from rest_framework import serializers
from curricula.models import LearningUnit



class LearningUnitSimpleSerializer(serializers.ModelSerializer):

    question_count = serializers.SerializerMethodField()
    test_id = serializers.SerializerMethodField()

    class Meta:
        model = LearningUnit
        fields = ('id', 'name', 'question_count', 'test_id')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }

    def get_question_count(self, instance):
        if instance.test:
            test = instance.test.first()

            if test:
                return test.test.questions.count()

        return 0

    def get_test_id(self, instance):
        if instance.test:
            test = instance.test.first()

            if test:
                return test.id

        return 0
