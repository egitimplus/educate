from rest_framework import viewsets, mixins
from rest_framework.response import Response
from companies.models import Classroom
from companies.serializers import ClassroomSerializer
from companies.permissions import ClassroomPermissionMixin
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
        course = self.get_object()
        cr = CourseRepository(course=course)
        cr.request = request
        content = cr.detail()

        return Response(content)

    # kullanıcının kayıtlı olduğu kursları listeler
    def course_user(self, request):
        queryset = Classroom.objects.filter(student=request.user).all()
        ids = queryset.values_list('id', flat=True)

        return Response(ids)

    # seçilmiş olan dersin ünite ve konularını listeler
    def course_lesson(self, request, pk=None):
        instance = self.get_object()
        cr = CourseRepository(course=instance)
        cr.request = request
        cr.publisher_id = int(request.query_params.get('publisher_id', None))
        cr.lesson_id = int(request.query_params.get('lesson_id', None))
        content = cr.lesson()

        return Response(content)

    # seçilmiş olan ünitenin konularını ve bölümlerini listeler
    def course_unit(self, request, pk=None):
        course = self.get_object()
        cr = CourseRepository(course=course)
        cr.request = request
        cr.publisher_id = int(request.query_params.get('p', None))
        cr.unit_id = int(request.query_params.get('u', None))
        content = cr.unit()

        return Response(content)

    # lecture okundu olarak düzenler
    def course_lecture_stat(self, request, pk=None):
        course = self.get_object()
        cr = CourseRepository(course=course)
        cr.request = request
        cr.lecture_id = int(request.query_params.get('lc', None))
        content = cr.lecture_stat()

        return Response({'data': content})

    # kurs soru parçalarının istatistikleri
    def course_component_stats(self, request, pk=None):
        course = self.get_object()
        cr = CourseRepository(course=course)
        cr.request = request
        content = cr.component_stats()

        return Response(content)

    # kurs bölümlerinin istatistikleri
    def course_lecture_stats(self):
        pass

