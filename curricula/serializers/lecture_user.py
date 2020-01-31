from rest_framework import serializers
from curricula.models import LearningLectureStat, LearningLecture, LearningLectureVideo, LearningLectureLiveScribe, LearningLectureText, LearningLectureYoutube
from .lecture_content import LearningLectureLiveScribeSerializer, LearningLectureVideoSerializer, LearningLectureTextSerializer, LearningLectureYoutubeSerializer
from generic_relations.relations import GenericRelatedField
from tests.models import Test


class LearningLectureUserSerializer(serializers.ModelSerializer):

    lecture_stat = serializers.SerializerMethodField()
    practice = serializers.SerializerMethodField()

    content_object = GenericRelatedField({
        LearningLectureVideo: LearningLectureVideoSerializer(),
        LearningLectureLiveScribe: LearningLectureLiveScribeSerializer(),
        LearningLectureText: LearningLectureTextSerializer(),
        LearningLectureYoutube: LearningLectureYoutubeSerializer(),
    })

    class Meta:
        model = LearningLecture
        fields = ('id', 'name', 'summary', 'content', 'position', 'content_object', 'lecture_stat', 'practice',
                  'created', 'updated')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }

    def get_lecture_stat(self, lecture):
        lecture_stat = {}
        user = self.context['request'].user
        if user.id:
            queryset = LearningLectureStat.objects.filter(user=user, lecture=lecture).first()
            lecture_stat = {'lecture_status': queryset.lecture_status, 'practice_status': queryset.practice_status}

        return lecture_stat

    def get_practice(self, lecture):
        practice = {}
        if lecture.practice_id:
            queryset = Test.objects.prefetch_related('question').filter(id=lecture.practice_id).first()

            practice = {'name': queryset.name, 'question_count': queryset.questions.count()}

        return practice
