from rest_framework import serializers
from companies.models import Classroom, School


class ClassroomSerializer(serializers.ModelSerializer):

    school_id = serializers.IntegerField(required=False)

    class Meta:
        model = Classroom
        fields = ('id', 'name', 'school_id', 'active', 'grade', 'department_id', 'year', 'created', 'updated')
        extra_kwargs = {
            'slug': {'required': False},
            'year': {'required': False},
        }

    def validate_school_id(self, value):
        school = School.objects.filter(id=value).exists()

        if not school:
            raise serializers.ValidationError('Seçilen okul bulunamadı.')

        return value

    def create(self, validated_data):
        classroom = Classroom.objects.create(**validated_data)

        return classroom

    def update(self, instance, validated_data):

        instance.name = validated_data['name']
        instance.active = validated_data['active']
        instance.grade = validated_data['grade']
        instance.department_id = validated_data['department_id']
        instance.save()

        return instance
