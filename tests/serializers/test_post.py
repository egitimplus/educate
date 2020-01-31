from rest_framework import serializers
from tests.models import Test
from educategories.models import EduCategory
from questions.models import Question
from django.db import transaction


class TestPostSerializer(serializers.ModelSerializer):

    questions = serializers.ListField(default=[], required=False, child=serializers.IntegerField())
    categories = serializers.ListField(default=[], required=False, child=serializers.IntegerField())

    publisher_id = serializers.IntegerField(required=True)

    class Meta:
        model = Test
        fields = ('id', 'name', 'active', 'test_seconds', 'categories', 'questions', 'test_type_id', 'publisher_id',
                  'created', 'updated')

    def validate_categories(self, value):
        categories = set(value)

        # kaynak seçilmiş mi kontrolü
        if categories:
            # kaynaklar veritabanında kayıtlı mı kontrolü
            categories_db_count = EduCategory.objects.filter(id__in=categories).count()
            categories_count = len(categories)

            if categories_db_count != categories_count:
                raise serializers.ValidationError('Seçilen bazı kategoriler bulunamadı.')
        else:
            raise serializers.ValidationError('Kategori seçimi yapmalısınız.')

        return value

    def validate_questions(self, value):
        questions = set(value)

        # kaynak seçilmiş mi kontrolü
        if questions:
            # kaynaklar veritabanında kayıtlı mı kontrolü
            questions_db_count = Question.objects.filter(id__in=questions).count()
            questions_count = len(questions)

            if questions_db_count != questions_count:
                raise serializers.ValidationError('Seçilen bazı sorular bulunamadı.')
        else:
            raise serializers.ValidationError('Soru seçimi yapmalısınız.')

        return value

    @transaction.atomic
    def create(self, validated_data):

        question_data = validated_data.pop('questions', None)
        category_data = validated_data.pop('categories', None)

        test = Test.objects.create(**validated_data)

        if question_data:
            self.create_categories(test, category_data)

        if category_data:
            self.create_questions(test, question_data)

        return validated_data

    @transaction.atomic
    def update(self, instance, validated_data):
        question_data = validated_data.pop('questions', None)
        category_data = validated_data.pop('categories', None)

        instance.save()

        self.update_categories(instance, category_data)
        self.update_questions(instance, question_data)

        return validated_data

    def create_categories(self, instance, data):

        for category in set(data):
            instance.categories.add(category)

    def create_questions(self, instance, data):

        for question in set(data):
            instance.questions.add(question)

    def update_categories(self, instance, data):
        test = Test.objects.filter(id=instance.id).first()

        old_categories = test.categories.values_list('id', flat=True);
        new_categories = data

        delete_categories = set(old_categories).difference(new_categories)
        add_categories = set(new_categories).difference(old_categories)



    def update_questions(self, instance, data):
        test = Test.objects.filter(id=instance.id).first()

        old_questions = test.questions.values_list('id', flat=True);
        new_questions = data

        delete_questions = set(old_questions).difference(new_questions)
        add_questions = set(new_questions).difference(old_questions)

        for d in delete_questions:
            instance.questions.remove(d)

        for a in add_questions:
            instance.questions.add(a)