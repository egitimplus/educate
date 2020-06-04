from rest_framework import serializers
from questions.models import Question, QuestionAnswer, QuestionExam, QuestionUnique
from educategories.serializers import EduCategorySerializer
from publishers.serializers import SourceSerializer
from django.db import transaction
from publishers.models import Source, Publisher
from components.models import Component, ComponentAnswer
from educategories.models import EduCategory
from library.models import Exam
from questions.serializers import QuestionAnswerPostSerializer
from questions.feeds import QuestionRepository


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'name', 'level', 'question_start_type', 'question_start_value', 'question_answer_type',
                  'edu_category', 'publisher','question_answer_value', 'question_pattern', 'active', 'seconds', 'created', 'updated')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        if kwargs.get('data', False):
            self.fields['question_answers'] = QuestionAnswerPostSerializer(many=True)

            self.fields['components'] = serializers.ListField(
                default=[],
                required=False,
                child=serializers.IntegerField()
            )
            self.fields['publishers'] = serializers.ListField(
                default=[],
                required=False,
                child=serializers.IntegerField()
            )
            self.fields['changes'] = serializers.DictField(
                default={},
                required=False,
                child=serializers.IntegerField()
            )
            self.fields['exams'] = serializers.ListField(
                default={},
                required=False,
                child=serializers.DictField(
                    default={},
                    required=False,
                    child=serializers.IntegerField()
                )
            )
        else:
            self.fields['edu_category'] = EduCategorySerializer(many=False)
            self.fields['answers'] = QuestionAnswerPostSerializer(many=True, context=self.context)
            self.fields['source_questions'] = SourceSerializer(many=True, context={'question': True})

    def validate_components(self, value):
        # TODO FRONTEND Sorular için soru tipi seçimini zorunlu tutmadık.
        components = set(value)

        if components:
            # componentler veritabanında kayıtlı mı kontrolü
            component_db_count = Component.objects.filter(id__in=components).count()
            component_count = len(components)

            if component_db_count != component_count:
                raise serializers.ValidationError('Seçilen bazı soru tipleri  bulunamadı.')

        return value

    def validate_publishers(self, value):
        publishers = set(value)

        # kaynak seçilmiş mi kontrolü
        if publishers:
            # kaynaklar veritabanında kayıtlı mı kontrolü
            source_db_count = Source.objects.filter(id__in=publishers).count()
            publisher_count = len(publishers)

            if source_db_count != publisher_count:
                raise serializers.ValidationError('Seçilen bazı kaynaklar bulunamadı.')
        else:
            raise serializers.ValidationError('Kaynak seçimi yapmalısınız.')

        return value

    def validate_publisher(self, value):
        publisher = Publisher.objects.filter(id=value).exists()

        if not publisher:
            raise serializers.ValidationError('Yayınevi bulunamadı.')

        return value

    def validate_exams(self, value):
        exams = set()

        if value:
            for exam in value:
                exams.add(exam['id'])

        exam_count = len(exams)

        if exam_count:
            # sınavlar veritabanında kayıtlı mı kontrolü
            exam_db_count = Exam.objects.filter(id__in=exams).count()

            if exam_db_count != exam_count:
                raise serializers.ValidationError('Seçilen bazı sınavlar bulunamadı.')

        return value

    def validate_edu_category_id(self, value):
        # kategoriler veritabanında kayıtlı mı kontrolü
        edu_category = EduCategory.objects.filter(id=value).exists()

        if not edu_category:
            raise serializers.ValidationError('Seçilen bazı kategoriler bulunamadı.')

        return value

    def validate_question_answers(self, value):
        """
        #-----------------------------------------------------------------------------
        # TODO BACKEND + FRONTEND Soru çeşidine göre birden fazla doğru cevap olabilir.
        #-----------------------------------------------------------------------------
        # En az iki cevap var mı
        # Doğru cevap işaretlenmiş mi
        # Yanlış cevap işaretlenmiş mi
        # Doğru cevap birtane mi
        # Componentler veritabanında mevcut mu
        # Aynı componentler hem doğru hem yanlış olarak seçilmiş mi
        #-----------------------------------------------------------------------------
        """
        question_answer_count = len(value)

        # En az iki cevap var mı
        if question_answer_count < 2:
            raise serializers.ValidationError('Soru cevap sayısı 2 den az olamaz.')

        true_answer_count = 0
        components = []
        for question_answer in value:

            if len(question_answer['true_components']) > 0:
                components.extend(question_answer['true_components'])

            if len(question_answer['false_components']) > 0:
                components.extend(question_answer['false_components'])

            if question_answer['is_true_answer'] == 1:
                true_answer_count = true_answer_count + 1

            # Aynı componentler hem doğru hem yanlış olarak seçilmiş mi
            same_values = set(question_answer['true_components']).intersection(question_answer['false_components'])
            if same_values:
                raise serializers.ValidationError('Aynı soru tipi hem doğru hem de yanlış soru tiplerinde olamaz.')

        # Doğru cevap işaretlenmiş mi
        if true_answer_count == 0:
            raise serializers.ValidationError('En az bir doğru cevap seçilmelidir.')

        # Doğru cevap birtane mi
        if true_answer_count > 1:
            raise serializers.ValidationError('Sadece bir doğru cevap seçilebilir.')

        # Yanlış cevap işaretlenmiş mi
        false_answer_count = question_answer_count - true_answer_count

        if false_answer_count == 0:
            raise serializers.ValidationError('En az bir yanlış cevap seçilmelidir.')

        # Componentler veritabanında mevcut mu
        components = set(components)
        component_count = len(components)
        component_db_count = Component.objects.filter(id__in=components).count()

        if component_db_count != component_count:
            raise serializers.ValidationError('Seçilen bazı soru tipleri bulunamadı.')

        return value

    def validate(self, attrs):
        # TODO FRONTEND validasyonlarını düzeltmek gerekli
        # daha önceden bu soru için çözüm yapılmış mı
        # eğer çözüm var ise soru güncellemeye kapatılacak
        if self.instance:
            qr = QuestionRepository(question=self.instance)

            if qr.have_answer_stat():
                raise serializers.ValidationError(
                    {'update': 'Bu soru için daha önceden çözüm yapılmış. Bu soru bilgileri güncellemeye kapalıdır.'}
                )

        return attrs

    @transaction.atomic
    def create(self, validated_data):

        # ilişkili alanları validated_data dan çıkartalım
        component_data = validated_data.pop('components', None)
        sources_data = validated_data.pop('publishers', None)
        exams_data = validated_data.pop('exams', None)
        answers_data = validated_data.pop('question_answers', None)
        changes = validated_data.pop('changes', None)

        # question tablosuna ekleme işlemi
        question = Question.objects.create(**validated_data)

        if component_data:
            self.create_components(question, component_data)

        if sources_data:
            self.create_sources(question, sources_data)

        if exams_data:
            self.create_exams(question, exams_data)

        if answers_data:
            self.create_answers(question, answers_data)

        return validated_data

    @transaction.atomic
    def update(self, instance, validated_data):
        # TODO Frontend : Eğer soru çözülmüş ise güncelleme ve silme kapalı olmalı. Sadece pasifleştirme yapılabilmeli.
        component_data = validated_data.pop('components', None)
        sources_data = validated_data.pop('publishers', None)
        exams_data = validated_data.pop('exams', None)
        answers_data = validated_data.pop('question_answers', None)
        changes = validated_data.pop('changes', None)

        if changes['general']:
            instance.level = validated_data['level']
            instance.seconds = validated_data['seconds']
            instance.active = validated_data['active']
            instance.edu_category_id = validated_data['edu_category_id']

            # question tablosu güncelleme işlemi
            instance.save()

        if changes['components']:
            self.create_components(instance, component_data)

        if changes['publishers']:
            self.create_sources(instance, sources_data)

        if changes['exams']:
            self.create_exams(instance, exams_data)

        if changes['answers']:
            self.create_answers(instance, answers_data)

        return validated_data

    def create_components(self, instance, data):

        old_components = Question.objects.prefetch_related('component').filter(id=instance.id).first()
        old_component_ids = old_components.component.values_list('id', flat=True)

        components = set(data)

        add_components = components.difference(old_component_ids)
        del_components = set(old_component_ids).difference(components)

        # ilişkili soru parçalarını veritabanına ekleyelim
        for del_component in del_components:
            instance.component.remove(del_component)

        for add_component in add_components:
            instance.component.add(add_component)

        # benzersiz soruları ekleyelim
        question_code = '-'.join(map(str, sorted(components)))

        question_unique = QuestionUnique.objects.filter(question_code=question_code).first()

        if question_unique:
            question_unique_id = question_unique.id
        else:
            new_question_unique = QuestionUnique.objects.create(question_code=question_code)
            question_unique_id = new_question_unique.id

        instance.question_unique_id = question_unique_id
        instance.save()

    def create_sources(self, instance, data):

        instance.source_questions.clear()

        # ilişkili kaynakları veritabanına ekleyelim
        for source in set(data):
            instance.source_questions.add(source)

    def create_exams(self, instance, data):

        # ilişkili sınav bilgilerini veritabanına ekleyelim
        # TODO aynı kayıt birden fazla varsa ?

        QuestionExam.objects.filter(question_id=instance.id).delete()

        for exam in data:
            QuestionExam.objects.create(question=instance, exam_id=exam['id'], exam_year=exam['exam_year'])

    def create_answers(self, instance, data):

        # question_answer tablosuna ekleme işlemi
        # TODO aynı kayıt birden fazla varsa ? Bunun kontrolünü yapmak gerekir.
        # TODO aynı cevap bir kere eklenebilmeli

        # ComponentAnswer.objects.filter(question_answer__question_id=instance.id).delete()
        QuestionAnswer.objects.filter(question_id=instance.id).delete()

        for answer_data in data:

            true_qt = answer_data.pop('true_components')
            false_qt = answer_data.pop('false_components')

            answer = QuestionAnswer.objects.create(question=instance, **answer_data)

            if answer_data['is_true_answer'] == 1:
                question_answer_id = answer.id

            for t in true_qt:
                ComponentAnswer.objects.create(component_id=t, question_answer=answer, component_ok=1)

            for f in false_qt:
                ComponentAnswer.objects.create(component_id=f, question_answer=answer, component_ok=0)

        # question tablosundai question_answer_id güncellemesini yapalım
        # TODO FRONTEND + BACKEND question_answer_id kaldırabiliriz.

        instance.question_answer_id = question_answer_id
        instance.save()




