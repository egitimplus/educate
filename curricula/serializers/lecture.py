from rest_framework import serializers
from curricula.models import LearningLectureStat, LearningLecture, LearningLectureVideo, LearningLectureLiveScribe, LearningLectureText, LearningLectureYoutube
from .lecture_content import LearningLectureLiveScribeSerializer, LearningLectureVideoSerializer, LearningLectureTextSerializer, LearningLectureYoutubeSerializer
from generic_relations.relations import GenericRelatedField
from tests.models import Test
from .lecture_stat import LearningLectureStatSerializer
from .test import LearningTestSerializer


class LearningLectureSerializer(serializers.ModelSerializer):

    practice = serializers.SerializerMethodField()
    stat = serializers.SerializerMethodField()
    test = LearningTestSerializer(many=True, required=False)
    subject_id = serializers.IntegerField(required=True)
    publisher_id = serializers.IntegerField(required=True)

    content_object = GenericRelatedField({
        LearningLectureVideo: LearningLectureVideoSerializer(),
        LearningLectureLiveScribe: LearningLectureLiveScribeSerializer(),
        LearningLectureText: LearningLectureTextSerializer(),
        LearningLectureYoutube: LearningLectureYoutubeSerializer(),
    })

    class Meta:
        model = LearningLecture
        fields = ('id', 'name', 'summary', 'content', 'position', 'content_object', 'practice', 'subject_id',
                  'publisher_id', 'created', 'updated', 'stat', 'test')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }

    def get_practice(self, lecture):
        practice = {}
        if lecture.practice_id:
            queryset = Test.objects.prefetch_related('questions').filter(id=lecture.practice_id).first()

            test_result = 0

            result_query = queryset.tests.order_by('-id').first()
            if result_query:
                test_result = result_query.test_result

            practice = {
                'id': queryset.id,
                'name': queryset.name,
                'question_count': queryset.questions.count(),
                'test_result': test_result
            }

        return practice

    def get_stat(self, lecture):

        request = self.context.get("request")
        queryset = LearningLectureStat.objects.filter(lecture=lecture, user_id=request.user.id).first()
        serializer = LearningLectureStatSerializer(queryset, many=False)

        return serializer.data
