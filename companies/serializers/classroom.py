from rest_framework import serializers
from companies.models import Classroom, School


class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = ('id', 'name', 'school', 'active', 'grade', 'department_id', 'year', 'created', 'updated','type')
        extra_kwargs = {
            'slug': {'required': False},
            'year': {'required': False},
        }

    def update(self, instance, validated_data):

        instance.name = validated_data['name']
        instance.active = validated_data['active']
        instance.grade = validated_data['grade']
        instance.department_id = validated_data['department_id']
        instance.save()

        return instance
