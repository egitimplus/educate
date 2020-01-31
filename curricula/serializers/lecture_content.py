from rest_framework import serializers
from curricula.models import LearningLectureYoutube, LearningLectureVideo, LearningLectureLiveScribe, LearningLectureText
from library.models import Media


class LearningLectureVideoSerializer(serializers.ModelSerializer):

    media = serializers.SerializerMethodField()

    class Meta:
        model = LearningLectureVideo
        fields = ('id', 'media')

    def get_media(self, lecture_content):
        media = {}
        if lecture_content.media_id:
            queryset = Media.objects.filter(id=lecture_content.media_id).first()

            media = {'id': queryset.id, 'name': queryset.media_name, 'desc': queryset.media_desc,
                     'file': queryset.media_file.url, 'type': 'video'}

        return media


class LearningLectureLiveScribeSerializer(serializers.ModelSerializer):

    media = serializers.SerializerMethodField()

    class Meta:
        model = LearningLectureLiveScribe
        fields = ('id', 'media')

    def get_media(self, lecture_content):
        media = {}
        if lecture_content.media_id:
            try:
                queryset = Media.objects.filter(id=lecture_content.media_id).first()
                media = {'id': queryset.id, 'name': queryset.media_name, 'desc': queryset.media_desc,
                         'file': queryset.media_file.url, 'type': 'livescribe'}
            except Exception as e:
                media = {}

        return media


class LearningLectureTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = LearningLectureText
        fields = ('id', 'content')


class LearningLectureYoutubeSerializer(serializers.ModelSerializer):

    type = serializers.CharField(default='youtube')

    class Meta:
        model = LearningLectureYoutube
        fields = ('id', 'name', 'desc', 'file', 'type')
