from rest_framework import serializers
from educategories.models.educategory import EduCategory


class EduCategorySerializer(serializers.ModelSerializer):

    parent_id = serializers.IntegerField(required=False, allow_null=True)
    lesson_id = serializers.IntegerField(required=False, allow_null=True)
    subject_id = serializers.IntegerField(required=False, allow_null=True)
    unit_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = EduCategory
        fields = ('id', 'name', 'depth', 'active', 'slug', 'sort_category', 'parent_id', 'lesson_id', 'subject_id',
                  'unit_id', 'created', 'updated')

        extra_kwargs = {
            'depth': {'required': False},
            'active': {'required': False},
            'slug': {'required': False},
            'sort_category': {'required': False},
        }

    def validate_parent_id(self, value):

        if value:
            # kategoriler veritabanında kayıtlı mı kontrolü
            edu_category = EduCategory.objects.filter(id=value).exists()

            if not edu_category:
                raise serializers.ValidationError('Seçilen üst kategori bulunamadı.')

            return value

    def create(self, validated_data):

        parent_id = validated_data.get('parent_id', 0)

        if parent_id:
            parent = EduCategory.objects.filter(id=parent_id).first()

            depth = int(parent.depth) + 1

            if depth == 1:
                lesson_id = parent.id
                unit_id = None
                subject_id = None
            elif depth == 2:
                lesson_id = parent.lesson_id
                unit_id = parent.id
                subject_id = None
            elif depth == 3:
                lesson_id = parent.lesson_id
                unit_id = parent.unit_id
                subject_id = parent.id

            add_category = EduCategory(
                name=validated_data['name'],
                depth=depth,
                active=validated_data['active'],
                parent_id=parent_id,
                lesson_id=lesson_id,
                unit_id=unit_id,
                subject_id=subject_id,
            )

        else:
            add_category = EduCategory(
                name=validated_data['name'],
                active=validated_data['active']
            )

        add_category.save()
        return add_category

    def update(self, instance, validated_data):

        instance.name = validated_data['name']
        instance.active = validated_data['active']
        instance.save()

        return instance
