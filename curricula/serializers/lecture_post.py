from rest_framework import serializers
from curricula.models import LearningLecture, LearningLectureVideo, LearningLectureLiveScribe, LearningLectureYoutube
from tests.models import Test
from library.models import Media
from django.db import transaction
from publishers.models import Publisher
from django.contrib.contenttypes.models import ContentType
from components.models import Component


class LearningLecturePostSerializer(serializers.ModelSerializer):

    media_id = serializers.IntegerField(required=True)
    media_type = serializers.CharField(required=True)
    media_name = serializers.CharField(required=False)
    media_desc = serializers.CharField(required=False)
    media_file = serializers.CharField(required=False)

    practice_id = serializers.IntegerField(default=None)
    subject_id = serializers.IntegerField(required=True)
    publisher_id = serializers.IntegerField(required=True)
    sub_components = serializers.ListField(
        default=[],
        required=False,
        child=serializers.IntegerField()
    )

    class Meta:
        model = LearningLecture
        fields = ('id', 'name', 'summary', 'content', 'position', 'practice_id', 'subject_id',
                  'publisher_id', 'sub_components', 'media_id', 'media_type', 'media_desc', 'media_name', 'media_file')

    def validate_publisher_id(self, value):
        publisher = Publisher.objects.filter(id=value).exists()

        if not publisher:
            raise serializers.ValidationError('Seçilen yayınevi bulunamadı.')

        return value

    def validate_practice_id(self, value):

        if value:
            practice = Test.objects.filter(id=value).exists()

            if not practice:
                raise serializers.ValidationError('Seçilen test bulunamadı.')

        return value

    def validate_media_type(self, value):

        if value != 'livescribe' and value != 'video' and value != 'youtube':
            raise serializers.ValidationError('Desteklenmeyen media tipi seçtiniz.')

        return value

    def validate_sub_components(self, value):
        components = set(value)

        if components:
            # componentler veritabanında kayıtlı mı kontrolü
            component_db_count = Component.objects.filter(id__in=components).count()
            component_count = len(components)

            if component_db_count != component_count:
                raise serializers.ValidationError('Seçilen bazı soru tipleri  bulunamadı.')

        return value

    def validate(self, data):

        if data['media_type'] != 'youtube':
            media = Media.objects.filter(id=data['media_id']).exists()

            if not media:
                raise serializers.ValidationError('Seçilen medya bulunamadı.')

        return data

    @transaction.atomic
    def create(self, validated_data):

        media_id = validated_data.pop('media_id', None)
        media_type = validated_data.pop('media_type', None)
        media_name = validated_data.pop('media_name', None)
        media_desc = validated_data.pop('media_desc', None)
        media_file = validated_data.pop('media_file', None)
        sub_components = validated_data.pop('sub_components', None)

        media = {
            'id': media_id,
            'name': media_name,
            'desc': media_desc,
            'type': media_type,
            'file': media_file
        }

        content = self.create_content_type(media)

        if validated_data['practice_id'] == 0:
            validated_data['practice_id'] = None

        validated_data['object_id'] = content['object_id']
        validated_data['content_type_id'] = content['content_type_id']

        print(validated_data)

        lecture = LearningLecture.objects.create(**validated_data)

        self.create_components(lecture, sub_components)

        return validated_data

    @transaction.atomic
    def update(self, instance, validated_data):

        # ilişkili alanları validated_data dan çıkartalım
        media_id = validated_data.pop('media_id', None)
        media_type = validated_data.pop('media_type', None)
        media_name = validated_data.pop('media_name', None)
        media_desc = validated_data.pop('media_desc', None)
        media_file = validated_data.pop('media_file', None)
        sub_components = validated_data.pop('sub_components', None)

        if validated_data['practice_id'] == 0:
            validated_data['practice_id'] = None

        media = {
            'id': media_id,
            'name': media_name,
            'desc': media_desc,
            'type': media_type,
            'file': media_file
        }

        content = self.create_content_type(media)

        instance.name = validated_data['name']
        instance.summary = validated_data['summary']
        instance.content = validated_data['content']
        instance.position = validated_data['position']
        instance.practice_id = validated_data['practice_id']
        instance.object_id = content['object_id']
        instance.content_type_id = content['content_type_id']

        instance.save()

        self.create_components(instance, sub_components)

        return validated_data

    def create_content_type(self, media):

        if media['type'] == 'livescribe':
            content = LearningLectureLiveScribe.objects.create(media_id=media['id'])

        elif media['type'] == 'video':
            content = LearningLectureVideo.objects.create(media_id=media['id'])

        elif media['type'] == 'youtube':
            id = media.pop('id', None)
            type = media.pop('type', None)

            content = LearningLectureYoutube.objects.create(**media)

        else:
            raise serializers.ValidationError('Desteklenmeyen media tipi seçtiniz.')

        content_type_id = ContentType.objects.get_for_model(content).id

        content = {
            'object_id': content.id,
            'content_type_id': content_type_id
        }
        return content

    def create_components(self, instance, data):

        if not data:
            instance.component.clear()
        else:
            old_components = LearningLecture.objects.prefetch_related('component').filter(id=instance.id).first()
            old_component_ids = old_components.component.values_list('id', flat=True)

            components = set(data)

            add_components = components.difference(old_component_ids)
            del_components = set(old_component_ids).difference(components)

            # ilişkili soru parçalarını veritabanına ekleyelim
            for del_component in del_components:
                instance.component.remove(del_component)

            for add_component in add_components:
                instance.component.add(add_component)

