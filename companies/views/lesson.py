from rest_framework import viewsets, mixins, status
from companies.models import Lesson, SchoolLessonTeacher
from companies.serializers import LessonSerializer, SchoolLessonTeacherSerializer
from companies.permissions import LessonPermissionMixin
from rest_framework.response import Response


class LessonViewSet(LessonPermissionMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    # okuldaki derse öğretmen ekler
    def attach_lesson_teacher(self, request, pk=None):
        # TODO ÇOK ÖNEMLİ!
        # TODO Ders eklerken sınıfa bir müfredat birkere eklenebilmeli
        # SIGNAL : Pattern listesine signal ile ekleme yapılıyor
        # SIGNAL : Role listesine signal ile ekleme yapılıyor

        self.get_object()
        serializer = SchoolLessonTeacherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # okuldaki dersten öğretmen siler
    def detach_lesson_teacher(self, request, pk=None):
        # SIGNAL : Pattern listesinden signal ile silme yapılıyor
        # SIGNAL : Role listesinden signal ile silme yapılıyor

        self.get_object()
        lesson_teacher_id = request.data.get('lesson_teacher_id')
        instance = SchoolLessonTeacher.objects.get(id=lesson_teacher_id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        # TODO Eğer sınıflara eklenmedi ise detach yapılabilir. Sınıflara eklenen dersler ne yapılacak ?
        # TODO Sınıfa eklenmiş ise tüm bilgilerin silineceği uyarısı yapılmalı.

    # okuldaki derse atanmış öğretmeni değiştirir
    def update_lesson_teacher(self, request, pk=None):
        # TODO : Pattern listesine signal ile ekleme ve silme yapılmalı
        # TODO : Eğer başka yoksa role listesine signal ile ekleme ve silme yapılmalı

        self.get_object()
        lesson_teacher_id = request.data.get('lesson_teacher_id')
        instance = SchoolLessonTeacher.objects.get(id=lesson_teacher_id)
        serializer = SchoolLessonTeacherSerializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # okuldaki derse öğretmen atanmış olanları listeler
    def list_lesson_teacher(self, request, pk=None):
        self.get_object()
        queryset = SchoolLessonTeacher.objects.select_related('teacher__teacher','publisher').filter(lesson_id=pk).all()

        response = []
        for data in queryset:
            response.append({
                'id': data.id,
                'name': data.name,
                'first_name': data.teacher.teacher.first_name,
                'last_name': data.teacher.teacher.last_name,
                'duration': data.duration,
                'publisher_name': data.publisher.name
            })
        return Response(response)
