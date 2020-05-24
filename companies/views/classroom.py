from rest_framework import viewsets, mixins
from companies.models import Classroom, SchoolStudent, SchoolTeacher, SchoolLessonTeacher, ClassroomLesson, ClassroomTeacher, ClassroomStudent
from companies.serializers import ClassroomSerializer
from companies.permissions import ClassroomPermissionMixin
from rest_framework.response import Response


class ClassroomViewSet(ClassroomPermissionMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    # sınıfa eklenmiş öğrencileri listeler
    def student_list(self, request, pk=None):
        classroom = self.get_object()

        queryset = ClassroomStudent.objects.select_related('student').filter(classroom=classroom).all()

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

        classroom = self.get_object()

        users = request.data.get('users')

        for user in users:

            ''' Okul öğrenci listesinde var mı ? '''
            school_student = SchoolStudent.objects.filter(school_id=classroom.school_id, student_id=user).exists()

            if school_student:

                class_student = ClassroomStudent.objects.filter(classroom=classroom, student_id=user).exists()

                if not class_student:
                    student = ClassroomStudent(classroom=classroom, student_id=user)
                    student.save()

        return Response({'message': 'Öğrenci güncellemesi tamamlandı.'})

    # sınıftan öğrenci siler
    def detach_student(self, request, pk=None):
        # SIGNAL : Pattern listesinden signal ile silme yapılıyor
        # SIGNAL : Role listesinden signal ile silme yapılıyor

        classroom = self.get_object()
        users = request.data.get('users')

        for user in users:
            ClassroomStudent.objects.filter(classroom=classroom, student_id=user).delete()

        return Response({'message': 'Öğrenci sınıftan silindi.'})

    # sınıfa eklenmiş öğretmenleri listeler
    def teacher_list(self, request, pk=None):
        classroom = self.get_object()
        queryset = ClassroomTeacher.objects.select_related('teacher').filter(classroom=classroom).all()

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

        classroom = self.get_object()

        users = request.data.get('users')

        for user in users:

            ''' Okul öğrenci listesinde var mı ? '''
            school_teacher = SchoolTeacher.objects.filter(school_id=classroom.school_id, teacher_id=user).exists()

            if school_teacher:

                class_teacher = ClassroomTeacher.objects.filter(classroom=classroom, teacher_id=user).exists()

                if not class_teacher:
                    teacher = ClassroomTeacher(classroom=classroom, teacher_id=user)
                    teacher.save()

        return Response({'message': 'Öğretmen güncellemesi tamamlandı.'})

    # sınıftan öğretmen siler
    def detach_teacher(self, request, pk=None):
        # SIGNAL : Pattern listesinden signal ile silme yapılıyor
        # SIGNAL : Role listesinden signal ile silme yapılıyor

        classroom = self.get_object()
        users = request.data.get('users')

        for user in users:
            ClassroomTeacher.objects.filter(classroom=classroom, teacher_id=user).delete()

        return Response({'message': 'Öğretmen sınıftan silindi.'})

    # sınıfa eklenmiş dersleri listeler
    def lesson_list(self, request, pk=None):
        classroom = self.get_object()

        queryset = ClassroomLesson.objects.select_related('lesson__teacher__teacher', 'lesson__lesson').filter(classroom=classroom).all()

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
        classroom = self.get_object()

        lesson_teachers = request.data.get('lesson_teachers')

        for lesson_teacher in lesson_teachers:

            school_lesson = SchoolLessonTeacher.objects.filter(id=lesson_teacher).exists()

            if school_lesson:

                class_lesson = ClassroomLesson.objects.filter(classroom=classroom, lesson_id=lesson_teacher).exists()

                if not class_lesson:
                    lesson = ClassroomLesson(classroom=classroom, lesson_id=lesson_teacher)
                    lesson.save()

        return Response({'message': 'Ders güncellemesi tamamlandı.'})

    # sınıftan ders siler
    def detach_lesson(self, request, pk=None):
        classroom = self.get_object()
        relation_id = request.data.get('lesson_teacher_id')
        ClassroomLesson.objects.filter(id=relation_id, classroom=classroom).delete()

        # TODO Ders sınıftan silindiğinde o ders ile ilgili bilgiler ne olacak ?
        # TODO Dersi alan öğrenciler olduğu unutulmamalı.

        return Response({'message': 'Ders sınıftan başarıyla silindi.'})
