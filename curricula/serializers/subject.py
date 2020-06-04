from rest_framework import serializers
from curricula.models import LearningSubject, LearningLectureStat
from .lecture import LearningLectureSerializer
from .lecture_stat import LearningLectureStatSerializer
from components.serializers import ComponentSerializer


class LearningSubjectListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        lesson = self.context.get('lesson', None)
        if lesson is not None:
            data = data.filter(lecture_parent__lesson__id=lesson)

        return super(LearningSubjectListSerializer, self).to_representation(data)


class LearningSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        list_serializer_class = LearningSubjectListSerializer
        model = LearningSubject
        fields = ('id', 'name', 'slug', 'content', 'position', 'unit', 'created', 'updated')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get("request")
        stat = self.context.get("stat")
        if request is not None and stat is not None:
            if request.user:
                self.fields['stat'] = serializers.SerializerMethodField(read_only=True)

        test = self.context.get('test', None)
        if test is not None:
            self.fields['test'] = serializers.SerializerMethodField(read_only=True)

        component = self.context.get('component', None)
        if component is not None:
            self.fields['component'] = serializers.SerializerMethodField(read_only=True)

        lecture = self.context.get('lecture', None)
        if lecture is not None:
            lesson = self.context.get('lesson', None)

            lecture['request'] = request
            lecture['lesson'] = lesson

            self.fields['lecture_parent'] = LearningLectureSerializer(read_only=True, many=True, context=lecture)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.content = validated_data['content']
        instance.position = validated_data['position']
        instance.save()
        return instance

    def get_stat(self, instance):
        request = self.context.get("request")
        publisher_id = self.context.get("publisher_id")

        if request is not None:
            if request.user:
                lectures = instance.lecture_parent.filter(publisher_id=publisher_id).all()
                ids = lectures.values_list('id', flat=True)

                queryset = LearningLectureStat.objects.filter(lecture_id__in=ids, user_id=request.user.id, lecture_status=1).all()
                serializer = LearningLectureStatSerializer(queryset, many=True, context=self.context)

                return serializer.data

        return {}

    def get_test(self, instance):
        lesson = self.context.get('lesson', None)

        test = instance.test.filter(lesson__id=lesson).order_by('-id').first()

        data = {}
        if test:
            data = {
                'id': test.id,
                'name': test.name,
                'question_count': test.questions.count(),
            }

        return data

    def get_component(self, instance):

        components = list()
        component_ids = list()

        lesson = self.context.get('lesson', None)

        test = instance.test.filter(lesson__id=lesson).first()

        if test:
            for question in test.questions.all():
                for question_component in question.components.all():
                    if question_component.id not in component_ids:
                        component = ComponentSerializer(question_component, many=False)
                        components.append(component.data)
                        component_ids.append(question_component.id)

        return components
