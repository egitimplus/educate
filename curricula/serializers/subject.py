from rest_framework import serializers
from curricula.models import LearningSubject, LearningUnit, LearningLectureStat
from .test import LearningTestSerializer
from .lecture import LearningLectureSerializer
from .lecture_stat import LearningLectureStatSerializer
from django.db.models import Count


class LearningSubjectSerializer(serializers.ModelSerializer):
    unit_id = serializers.IntegerField(required=False)
    # test = LearningTestSerializer(many=True, required=False)
    stat = serializers.SerializerMethodField(read_only=True)
    test = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = LearningSubject
        fields = ('id', 'name', 'slug', 'content', 'position', 'test', 'unit_id', 'created', 'updated', 'lecture_parent','stat')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['lecture_parent'] = LearningLectureSerializer(read_only=True, many=True, context=self.context)

    def validate_unit_id(self, value):
        unit = LearningUnit.objects.filter(id=value).exists()

        if not unit:
            raise serializers.ValidationError('Seçilen ünite bulunamadı.')

        return value

    def create(self, validated_data):
        subject = LearningSubject.objects.create(**validated_data)

        return subject

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.content = validated_data['content']
        instance.position = validated_data['position']
        instance.save()
        return instance

    def get_stat(self, subject):
        request = self.context.get("request")
        publisher_id = self.context.get("publisher_id")

        lectures = subject.lecture_parent.filter(publisher_id=publisher_id).all()
        ids = lectures.values_list('id', flat=True)

        queryset = LearningLectureStat.objects.filter(lecture_id__in=ids, user_id=request.user.id, lecture_status=1).all()
        serializer = LearningLectureStatSerializer(queryset, many=True, context=self.context)

        return serializer.data

    def get_test(self, subject):
        publisher_id = self.context.get("publisher_id")

        # TODO burası acaba sadece o publisher veriyormu kontrol edelim
        tests = subject.test.filter(test__publisher_id=publisher_id).first()

        serializer = LearningTestSerializer(tests, many=False)

        return serializer.data
