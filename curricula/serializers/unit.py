from rest_framework import serializers
from curricula.models import LearningLesson, LearningDomain, LearningUnit
from curricula.serializers import LearningTestSerializer, LearningSubjectSerializer


class LearningUnitSerializer(serializers.ModelSerializer):

    test = LearningTestSerializer(many=True)
    domain_id = serializers.IntegerField()
    lesson_id = serializers.IntegerField(required=False)

    class Meta:
        model = LearningUnit
        fields = ('id', 'name', 'slug', 'content', 'position', 'test', 'domain_id', 'lesson_id', 'component', 'created',
                  'updated', 'subjects')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['subjects'] = LearningSubjectSerializer(read_only=True, many=True, context=self.context)

    def validate_domain_id(self, value):
        domain = LearningDomain.objects.filter(id=value).exists()

        if not domain:
            raise serializers.ValidationError('Seçilen alan bulunamadı.')

        return value

    def validate_lesson_id(self, value):
        lesson = LearningLesson.objects.filter(id=value).exists()

        if not lesson:
            raise serializers.ValidationError('Seçilen ders bulunamadı.')

        return value

    def create(self, validated_data):
        unit = LearningUnit.objects.create(**validated_data)

        return unit

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.content = validated_data['content']
        instance.position = validated_data['position']
        instance.domain_id = validated_data['domain_id']

        instance.save()
        return instance

