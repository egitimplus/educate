from rest_framework import viewsets, mixins, status
from companies.models import Classroom, SchoolStudent, SchoolTeacher, SchoolLessonTeacher, ClassroomLesson, ClassroomTeacher, ClassroomStudent
from companies.serializers import ClassroomSerializer
from companies.permissions import ClassroomPermissionMixin
from rest_framework.response import Response
from companies.feeds import CourseRepository


class CourseViewSet(ClassroomPermissionMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

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
        course = CourseRepository(course=self.get_object())
        content = course.detail()

        return Response(content)

    # kullanıcının kayıtlı olduğu kursları listeler
    def course_user(self, request):
        queryset = Classroom.objects.filter(student=request.user).all()
        ids = queryset.values_list('id', flat=True)

        return Response(ids)

    # kurs soru parçalarının istatistikleri
    def course_stat(self, request, pk=None):
        course = CourseRepository(course=self.get_object())
        course.request = request
        content = course.stat()

        return Response(content)

    # seçilmiş olan dersin ünite ve konularını listeler
    def course_lesson(self, request, pk=None):
        course = CourseRepository(course=self.get_object())
        course.request = request
        course.publisher_id = int(request.query_params.get('publisher_id', None))
        course.lesson_id = int(request.query_params.get('lesson_id', None))
        content = course.lesson()

        return Response(content)

    # seçilmiş olan ünitenin konularını ve bölümlerini listeler
    def course_unit(self, request, pk=None):

        course = CourseRepository(course=self.get_object())
        course.request = request
        course.publisher_id = int(request.query_params.get('p', None))
        course.unit_id = int(request.query_params.get('u', None))
        content = course.unit()

        return Response(content)

    # lecture okundu olarak düzenler
    def course_lecture_stat(self, request, pk=None):
        course = CourseRepository(course=self.get_object())
        course.request = request
        course.lecture_id = int(request.query_params.get('lc', None))
        content = course.lecture_stat()

        return Response({'data': content})
