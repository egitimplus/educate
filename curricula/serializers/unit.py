from rest_framework import serializers
from curricula.models import LearningUnit
from curricula.serializers import LearningSubjectSerializer
from components.serializers import ComponentSerializer


class LearningUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = LearningUnit
        fields = ('id', 'name', 'slug', 'content', 'position', 'domain', 'lesson', 'created', 'updated')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False},
            'lesson': {'required': False}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        subject = self.context.get('subject', None)
        test = self.context.get('test', None)
        component = self.context.get('component', None)
        request = self.context.get('request', None)

        if subject is not None:
            subject['request'] = request
            self.fields['subjects'] = LearningSubjectSerializer(read_only=True, many=True, context=subject)

        if test is not None:
            self.fields['test'] = serializers.SerializerMethodField(read_only=True)

        if component is not None:
            self.fields['component'] = serializers.SerializerMethodField(read_only=True)

    def get_test(self, instance):
        publisher_id = self.context.get("publisher_id")

        # TODO burası acaba sadece o publisher veriyormu kontrol edelim
        test = instance.test.filter(test__publisher_id=publisher_id).order_by('-id').first()

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
        classroom = self.context.get("classroom")

        test = instance.test.filter(test__classroom_id=classroom).first()

        for question in test.questions.all():
            for question_component in question.components.all():
                if question_component.id not in component_ids:
                    component = ComponentSerializer(question_component, many=False)
                    components.append(component.data)
                    component_ids.append(question_component.id)

        return components
