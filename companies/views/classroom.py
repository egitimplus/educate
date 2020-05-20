from rest_framework import viewsets, mixins, status
from companies.models import Classroom, SchoolStudent, SchoolTeacher, SchoolLessonTeacher, ClassroomLesson, ClassroomTeacher, ClassroomStudent
from companies.serializers import ClassroomSerializer
from curricula.serializers import LearningLectureStatSerializer, LearningUnitSerializerWithSubjects, LearningSubjectSerializer
from companies.permissions import ClassroomPermissionMixin
from rest_framework.response import Response
from curricula.models import LearningSubject, LearningUnit, LearningLectureStat
from django.db.models import Count
from components.models import ComponentStat
from components.serializers import ComponentStatSerializer


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

        classroom = self.get_object()

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

        classroom = self.get_object()
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

        classroom = self.get_object()

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

        classroom = self.get_object()
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
        classroom = self.get_object()

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

    '''
    # react 
    # -----------------------------------------------------------------------------------------------------------------
    # list()                : kurs listesi
    # course()              : kurs derleri ve üniteleri
    # course_unit()         : kurs ünitesi, konuları ve bölümleri
    # course_user()         : kullanıcının kayıtlı kursları
    # course_lecture_stat() : lecture okundu olarak düzenler
    # course_stat()         : kurs soru tiplerinin istatistikleri
    # course_lesson()       : kurs dersi, üniteleri ve konuları - kulllanılmıyor
    '''

    # sınıfa eklenmiş dersleri ve üniteleri listeler
    def course(self, request, pk=None):
        self.get_object()

        queryset = ClassroomLesson.objects.select_related(
            'lesson__lesson__curricula'
        ).prefetch_related(
            'lesson__lesson__curricula__units__component'
        ).filter(classroom_id=pk).all()

        response = []
        item = {}
        content = {}

        for item in queryset:
            unit = LearningUnitSerializerWithSubjects(item.lesson.lesson.curricula.units.all(), many=True)

            components = list()

            for unit_item in item.lesson.lesson.curricula.units.all():
                unit_components = list(unit_item.component.values_list('id', flat=True))
                components = components + unit_components

            unique_components = list(set(components))

            response.append({
                'id': item.id,
                'period': item.lesson.duration,
                'name': item.lesson.name,
                'lesson_id': item.lesson.id,
                'lesson_name': item.lesson.lesson.name,
                'publisher_id': item.lesson.publisher_id,
                'curricula_id': item.lesson.lesson.curricula.id,
                'curricula_name': item.lesson.lesson.curricula.name,
                'unit': unit.data,
                'component': unique_components
            })

        if item:
            content = {
                'id': item.classroom.id,
                'name': item.classroom.name,
                'lessons': response
            }

        return Response(content)

    # seçilmiş olan dersin ünite ve konularını listeler
    def course_lesson(self, request, pk=None):

        row = ClassroomLesson.objects.select_related(
            'lesson__lesson__curricula'
        ).prefetch_related(
            'lesson__lesson__curricula__units'
        ).filter(pk=pk).first()

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

    # seçilmiş olan ünitenin konularını ve bölümlerini listeler
    def course_unit(self, request, pk=None):
        row = LearningUnit.objects.get(pk=pk)
        publisher_id = int(self.request.query_params.get('publisher_id', None))

        queryset = LearningSubject.objects.prefetch_related('lecture_parent').filter(unit_id=pk, lecture_parent__publisher_id=publisher_id).annotate(total=Count('unit_id')).all()
        serializer = LearningSubjectSerializer(queryset, many=True, context={'request': request, 'publisher_id': publisher_id})

        data = {
            'id': row.id,
            'name': row.name,
            'subjects': serializer.data
        }

        return Response(data)

    # kullanıcının kayıtlı olduğu kursları listeler
    def course_user(self, request):

        user = request.user

        queryset = Classroom.objects.filter(student=user).all()
        ids = queryset.values_list('id', flat=True)

        return Response(ids)

    # lecture okundu olarak düzenler
    def course_lecture_stat(self, request, pk=None):

        obj, created = LearningLectureStat.objects.update_or_create(
            user=request.user,
            lecture_id=pk,
            defaults={'lecture_status': 1},
        )

        serializer = LearningLectureStatSerializer(obj, many=False)
        return Response({'data': serializer.data})

    # kurs soru parçalarının istatistikleri
    def course_stat(self, request, pk=None):
        queryset = ClassroomLesson.objects.prefetch_related('lesson__lesson__curricula__units__component').filter(classroom_id=pk).all()

        e = list()

        for q in queryset:
            for u in q.lesson.lesson.curricula.units.all():
                d = list(u.component.values_list('id', flat=True))
                e = e + d

        components = (list(set(e)))

        stats = ComponentStat.objects.filter(component__in=components, user=request.user).all()

        serializer = ComponentStatSerializer(stats, many=True)
        return Response(serializer.data)

