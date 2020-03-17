from companies.models import SchoolLessonTeacher, Lesson, SchoolTeacher
from rest_framework import serializers


class SchoolLessonTeacherSerializer(serializers.ModelSerializer):

    lesson_id = serializers.IntegerField(required=False)
    teacher_id = serializers.IntegerField()
    publisher_id = serializers.IntegerField()

    class Meta:
        model = SchoolLessonTeacher
        fields = ('id', 'name', 'duration', 'lesson_id', 'teacher_id', 'publisher_id')

    def validate_lesson_id(self, value):
        # kullanıcı veritabanında kayıtlı mı kontrolü
        lesson = Lesson.objects.filter(id=value).exists()

        if not lesson:
            raise serializers.ValidationError('Seçilen ders bulunamadı.')

        return value

    def validate_teacher_id(self, value):
        # kullanıcı veritabanında kayıtlı mı kontrolü
        teacher = SchoolTeacher.objects.filter(id=value).exists()

        if not teacher:
            raise serializers.ValidationError('Seçilen okul öğretmeni bulunamadı.')

        return value

    def create(self, validated_data):
        lesson_teacher = SchoolLessonTeacher.objects.create(**validated_data)

        return lesson_teacher

    def update(self, instance, validated_data):

        instance.name = validated_data['name']
        instance.duration = validated_data['duration']
        instance.teacher_id = validated_data['teacher_id']
        instance.save()

        return instance