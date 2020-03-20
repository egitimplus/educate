from rest_framework import viewsets, mixins, status
from companies.models import Classroom, SchoolStudent, SchoolTeacher, SchoolLessonTeacher, ClassroomLesson, ClassroomTeacher, ClassroomStudent
from companies.serializers import ClassroomSerializer
from curricula.serializers import LearningUnitSimpleSerializer, LearningUnitSerializerWithSubjects
from companies.permissions import ClassroomPermissionMixin
from rest_framework.response import Response


class ClassroomViewSet(ClassroomPermissionMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    # sınıf siler
    def destroy(self, request, *args, **kwargs):
        # TODO Sınıf silindiğinde sınıf ve sınıf öğrencileri ile ilgili tüm bilgiler silinir.
        # TODO bunun uyarısını yapmak gerekli. Hatta güvenlik kodu gibi birşey olmalı.
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # sınıfa eklenmiş öğrencileri listeler
    def student_list(self, request, pk=None):
        self.get_object()
        queryset = ClassroomStudent.objects.select_related('student').filter(classroom_id=pk).all()

        response = []
        for item in queryset:

            response.append({
                'id': item.id,
                'user_id': item.student.id,
                'first_name': item.student.first_name,
                'last_name': item.student.last_name
            })

        return Response(response)

    # sınıfa öğrenci ekler
    def attach_student(self, request, pk=None):
        # SIGNAL : Pattern listesine signal ile ekleme yapılıyor
        # SIGNAL : Role listesine signal ile ekleme yapılıyor

        self.get_object()

        classroom = Classroom.objects.get(id=pk)
        users = request.data.get('users')

        for user in users:

            ''' Okul öğrenci listesinde var mı ? '''
            school_student = SchoolStudent.objects.filter(school_id=classroom.school_id, student_id=user).exists()

            if school_student:

                class_student = ClassroomStudent.objects.filter(classroom_id=pk, student_id=user).exists()

                if not class_student:
                    student = ClassroomStudent(classroom_id=pk, student_id=user)
                    student.save()

        return Response({'message': 'Öğrenci güncellemesi tamamlandı.'})

    # sınıftan öğrenci siler
    def detach_student(self, request, pk=None):
        # SIGNAL : Pattern listesinden signal ile silme yapılıyor
        # SIGNAL : Role listesinden signal ile silme yapılıyor

        self.get_object()
        classroom = Classroom.objects.get(id=pk)
        users = request.data.get('users')

        for user in users:
            ClassroomStudent.objects.filter(classroom_id=pk, student_id=user).delete()

        return Response({'message': 'Öğrenci sınıftan silindi.'})

    # sınıfa eklenmiş öğretmenleri listeler
    def teacher_list(self, request, pk=None):
        self.get_object()
        queryset = ClassroomTeacher.objects.select_related('teacher').filter(classroom_id=pk).all()

        response = []
        for item in queryset:

            response.append({
                'id': item.id,
                'user_id': item.teacher.id,
                'first_name': item.teacher.first_name,
                'last_name': item.teacher.last_name
            })

        return Response(response)

    # sınıfa öğretmen ekler
    def attach_teacher(self, request, pk=None):
        # SIGNAL : Pattern listesine signal ile ekleme yapılıyor
        # SIGNAL : Role listesine signal ile ekleme yapılıyor

        self.get_object()

        classroom = Classroom.objects.get(id=pk)
        users = request.data.get('users')

        for user in users:

            ''' Okul öğrenci listesinde var mı ? '''
            school_teacher = SchoolTeacher.objects.filter(school_id=classroom.school_id, teacher_id=user).exists()

            if school_teacher:

                class_teacher = ClassroomTeacher.objects.filter(classroom_id=pk, teacher_id=user).exists()

                if not class_teacher:
                    teacher = ClassroomTeacher(classroom_id=pk, teacher_id=user)
                    teacher.save()

        return Response({'message': 'Öğretmen güncellemesi tamamlandı.'})

    # sınıftan öğretmen siler
    def detach_teacher(self, request, pk=None):
        # SIGNAL : Pattern listesinden signal ile silme yapılıyor
        # SIGNAL : Role listesinden signal ile silme yapılıyor

        self.get_object()
        classroom = Classroom.objects.get(id=pk)
        users = request.data.get('users')

        for user in users:
            ClassroomTeacher.objects.filter(classroom_id=pk, teacher_id=user).delete()

        return Response({'message': 'Öğretmen sınıftan silindi.'})

    # sınıfa eklenmiş dersleri listeler
    def lesson_list(self, request, pk=None):
        self.get_object()

        queryset = ClassroomLesson.objects.select_related('lesson__teacher__teacher', 'lesson__lesson').filter(classroom_id=pk).all()

        response = []
        for item in queryset:
            response.append({
                'id': item.id,
                'period': item.lesson.duration,
                'name': item.lesson.name,
                'lesson_id': item.lesson.id,
                'lesson_name': item.lesson.lesson.name,
                'first_name': item.lesson.teacher.teacher.first_name,
                'last_name': item.lesson.teacher.teacher.last_name,
            })

        return Response(response)


    # sınıfa ders ekler
    def attach_lesson(self, request, pk=None):
        self.get_object()

        classroom = Classroom.objects.get(id=pk)
        lesson_teachers = request.data.get('lesson_teachers')

        for lesson_teacher in lesson_teachers:

            school_lesson = SchoolLessonTeacher.objects.filter(id=lesson_teacher).exists()

            if school_lesson:

                class_lesson = ClassroomLesson.objects.filter(classroom_id=pk, lesson_id=lesson_teacher).exists()

                if not class_lesson:
                    lesson = ClassroomLesson(classroom_id=pk, lesson_id=lesson_teacher)
                    lesson.save()

        return Response({'message': 'Ders güncellemesi tamamlandı.'})

    # sınıftan ders siler
    def detach_lesson(self, request, pk=None):
        self.get_object()
        relation_id = request.data.get('lesson_teacher_id')
        ClassroomLesson.objects.filter(id=relation_id).delete()

        # TODO Ders sınıftan silindiğinde o ders ile ilgili bilgiler ne olacak ?
        # TODO Dersi alan öğrenciler olduğu unutulmamalı.

        return Response({'message': 'Ders sınıftan başarıyla silindi.'})

    # react # kurs derleri ve üniteleri
    def course(self, request, pk=None):
        self.get_object()

        queryset = ClassroomLesson.objects.select_related('lesson__lesson__curricula').prefetch_related('lesson__lesson__curricula__units').filter(classroom_id=pk).all()

        response = []
        for item in queryset:
            unit = LearningUnitSimpleSerializer(item.lesson.lesson.curricula.units.all(), many=True)

            response.append({
                'id': item.id,
                'period': item.lesson.duration,
                'name': item.lesson.name,
                'lesson_id': item.lesson.id,
                'lesson_name': item.lesson.lesson.name,
                'publisher_id': item.lesson.publisher_id,
                'curricula_id': item.lesson.lesson.curricula.id,
                'curricula_name': item.lesson.lesson.curricula.name,
                'unit': unit.data
            })

        return Response(response)

    def course_lesson(self, request, pk=None):

        row = ClassroomLesson.objects.select_related('lesson__lesson__curricula').prefetch_related('lesson__lesson__curricula__units').filter(pk=pk).first()

        unit = LearningUnitSerializerWithSubjects(row.lesson.lesson.curricula.units.all(), many=True)


        response = {
            'id': row.id,
            'period': row.lesson.duration,
            'name': row.lesson.name,
            'lesson_id': row.lesson.id,
            'lesson_name': row.lesson.lesson.name,
            'publisher_id': row.lesson.publisher_id,
            'curricula_id': row.lesson.lesson.curricula.id,
            'curricula_name': row.lesson.lesson.curricula.name,
            'unit': unit.data
        }


        return Response(response)
