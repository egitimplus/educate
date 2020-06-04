from rest_framework import serializers
from curricula.models import LearningLectureStat, LearningLecture, LearningLectureVideo, LearningLectureLiveScribe, LearningLectureText, LearningLectureYoutube
from .lecture_content import LearningLectureLiveScribeSerializer, LearningLectureVideoSerializer, LearningLectureTextSerializer, LearningLectureYoutubeSerializer
from generic_relations.relations import GenericRelatedField
from tests.models import Test
from .lecture_stat import LearningLectureStatSerializer
from components.serializers import ComponentSerializer


class LearningLectureListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        lesson = self.context.get('lesson', None)
        if lesson is not None:
            data = data.filter(lesson__id=lesson)

        return super(LearningLectureListSerializer, self).to_representation(data)


class LearningLectureSerializer(serializers.ModelSerializer):

    content_object = GenericRelatedField({
        LearningLectureVideo: LearningLectureVideoSerializer(),
        LearningLectureLiveScribe: LearningLectureLiveScribeSerializer(),
        LearningLectureText: LearningLectureTextSerializer(),
        LearningLectureYoutube: LearningLectureYoutubeSerializer(),
    })

    class Meta:
        list_serializer_class = LearningLectureListSerializer
        model = LearningLecture
        fields = ('id', 'name', 'summary', 'content', 'position', 'content_object', 'created', 'updated', 'subject', 'publisher')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get("request")
        stat = self.context.get("stat")
        if request is not None and stat is not None:
            if request.user:
                self.fields['stat'] = serializers.SerializerMethodField()

        practice = self.context.get('practice', None)
        if practice is not None:
            self.fields['practice'] = serializers.SerializerMethodField()

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
        request = self.context.get('request')

        if request is not None:
            if request:
                queryset = LearningLectureStat.objects.filter(user=request.user, lecture=lecture).first()
                serializer = LearningLectureStatSerializer(queryset, many=False)
                return serializer.data

        return {}
