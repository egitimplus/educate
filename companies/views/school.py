from rest_framework import viewsets, mixins
from companies.models import Lesson, School, Classroom, SchoolLessonTeacher, SchoolManager, SchoolTeacher, SchoolStudent, SchoolUser, SchoolBook
from companies.serializers import SchoolSerializer, ClassroomSerializer, SchoolUserSerializer, LessonSerializer
from rest_framework.response import Response
from rest_framework import status
from companies.permissions import *
from django.contrib.auth import get_user_model
from library.feeds import DisableSignals


User = get_user_model()


class SchoolViewSet(SchoolPermissionMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, viewsets.GenericViewSet):

    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def update_school(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        instance.name = request.data.get('name')
        instance.type_id = request.data.get('type_id')
        instance.address = request.data.get('address')

        with DisableSignals():
            instance.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # okul siler
    def destroy(self, request, *args, **kwargs):
        # TODO okul silindiğinde okul ile ilgili kullanıcılara ait tüm bilgiler de silinir.
        # TODO bunun uyarısını yapmak gerekli. Hatta güvenlik kodu gibi birşey olmalı.
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # okula bağlı sınıfları listeler
    def classroom_list(self, request, pk=None):
        self.get_object()
        queryset = Classroom.objects.filter(school_id=pk).all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ClassroomSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ClassroomSerializer(queryset, many=True)
        return Response(serializer.data)

    # okula eklenmiş dersleri listeler
    def lesson_list(self, request, pk=None):
        self.get_object()
        queryset = Lesson.objects.filter(school_id=pk).all()

        serializer = LessonSerializer(queryset, many=True)
        return Response(serializer.data)

    # okuldaki öğretmen atanmış tüm dersleri listeler
    def lesson_teacher_list(self, request, pk=None):
        self.get_object()
        queryset = SchoolLessonTeacher.objects.select_related('teacher__teacher', 'lesson').filter(teacher__school_id=pk).all()
        response = []
        for item in queryset:

            data = {
                'id': item.id,
                'name': item.name,
                'school_teacher_id': item.teacher.id,
                'period': item.duration,
                'lesson': {
                    'id': item.lesson.id,
                    'name': item.lesson.name
                },
                'user': {
                    'id': item.teacher.teacher.id,
                    'first_name': item.teacher.teacher.first_name,
                    'last_name': item.teacher.teacher.last_name
                }
            }

            response.append(data)

        return Response(response)

    # okuldaki öğretmen atanmış dersleri listeler. Ders filtreli.
    def lesson_teacher_filter_list(self, request, pk=None):
        lesson_id = request.data.get('lesson_id')
        self.get_object()
        queryset = SchoolLessonTeacher.objects.select_related('teacher__teacher', 'lesson').filter(teacher__school_id=pk, lesson_id=lesson_id).all()
        response = []
        for item in queryset:

            data = {
                'id': item.id,
                'name': item.name,
                'school_teacher_id': item.teacher.id,
                'period': item.duration,
                'lesson': {
                    'id': item.lesson.id,
                    'name': item.lesson.name
                },
                'user': {
                    'id': item.teacher.teacher.id,
                    'first_name': item.teacher.teacher.first_name,
                    'last_name': item.teacher.teacher.last_name
                }
            }

            response.append(data)

        return Response(response)

    # okula atanmış yöneticileri listeler
    def manager_list(self, request, pk=None):
        self.get_object()
        queryset = School.objects.prefetch_related('manager').filter(id=pk).first()

        response = []
        for data in queryset.schoolmanager_set.all():
            response.append({
                'school_manager_id': data.id,
                'id': data.manager.id,
                'first_name': data.manager.first_name,
                'last_name': data.manager.last_name,
                'email': data.manager.email,
                'username': data.manager.username
            })
        return Response(response)

    # okula yönetici ekler
    def attach_manager(self, request, pk=None):
        # SIGNAL : Pattern listesine signal ile ekleme yapılıyor
        # SIGNAL : Role listesine signal ile ekleme yapılıyor

        self.get_object()
        user_id = request.data.get('user_id')

        manager_count = SchoolManager.objects.filter(school_id=pk, manager_id=user_id).exists()

        if manager_count:
            return Response({'error': 'Yönetici okula daha önce eklenmiş.'})

        school = School.objects.get(id=pk)
        user = User.objects.get(id=user_id)

        manager = SchoolManager(school=school, manager=user)
        manager.save()

        user_count = SchoolUser.objects.filter(school_id=pk, user_id=user_id).exists()

        if not user_count:
            user = SchoolUser(school=school, user=user)
            user.save()

        return Response({'message': 'Yönetici okula başarıyla eklendi.'})

    # okuldan yönetici siler
    def detach_manager(self, request, pk=None):
        # SIGNAL : Pattern listesinden signal ile silme yapılıyor
        # SIGNAL : Role listesinden signal ile silme yapılıyor

        self.get_object()
        relation_id = request.data.get('relation_id')
        manager = SchoolManager.objects.get(id=relation_id)
        manager.delete()

        return Response({'message': 'Yönetici okuldan başarıyla silindi.'})

    # okula eklenmiş öğrencileri listeler
    def student_list(self, request, pk=None):
        self.get_object()
        queryset = School.objects.prefetch_related('student').filter(id=pk).first()

        response = []
        for data in queryset.schoolstudent_set.all():
            response.append({
                'school_student_id': data.id,
                'id': data.student.id,
                'first_name': data.student.first_name,
                'last_name': data.student.last_name,
                'email': data.student.email,
                'username': data.student.username
            })
        return Response(response)

    # okula öğrenci ekler
    def attach_student(self, request, pk=None):

        self.get_object()
        user_id = request.data.get('user_id')

        student_count = SchoolStudent.objects.filter(school_id=pk, student_id=user_id).exists()

        if student_count:
            return Response({'error': 'Öğrenci okula daha önce eklenmiş.'})

        school = School.objects.get(id=pk)
        user = User.objects.get(id=user_id)

        student = SchoolStudent(school=school, student=user)
        student.save()

        user_count = SchoolUser.objects.filter(school_id=pk, user_id=user_id).exists()

        if not user_count:
            school_user = SchoolUser(school=school, user=user)
            school_user.save()

        return Response({'message': 'Öğrenci okula başarıyla eklendi.'})

    # okuldan öğrenci siler
    def detach_student(self, request, pk=None):

        self.get_object()
        relation_id = request.data.get('relation_id')
        manager = SchoolStudent.objects.get(id=relation_id)
        manager.delete()

        # TODO öğrenci sınıflarda var ise oralardanda kaydının silinmesi gerekli
        # TODO öğrenciye ait tüm bilgilerin de sistemden silinmesi gerekir.
        # TODO Öğrenci okuldan ayrıldı ise pasifleştirme işlemi yapılarak. Bilgilerin kalması sağlanabilir.
        # TODO Eğer öğrenci sınıf değiştirdi ise sınıf değiştirme yapmak gerekli.

        return Response({'message': 'Öğrenci okuldan başarıyla silindi.'})

    # okula eklenmiş öğretmenleri listeler
    def teacher_list(self, request, pk=None):
        self.get_object()
        queryset = School.objects.prefetch_related('teacher').filter(id=pk).first()

        response = []
        for data in queryset.schoolteacher_set.all():
            response.append({
                'school_teacher_id': data.id,
                'id': data.teacher.id,
                'first_name': data.teacher.first_name,
                'last_name': data.teacher.last_name,
                'email': data.teacher.email,
                'username': data.teacher.username
            })
        return Response(response)

    # okula öğretmen ekler
    def attach_teacher(self, request, pk=None):

        self.get_object()
        user_id = request.data.get('user_id')

        teacher_count = SchoolTeacher.objects.filter(school_id=pk, teacher_id=user_id).exists()

        if teacher_count:
            return Response({'error': 'Öğretmen okula daha önce eklenmiş.'})

        school = School.objects.get(id=pk)
        user = User.objects.get(id=user_id)

        teacher = SchoolTeacher(school=school, teacher=user)
        teacher.save()

        user_count = SchoolUser.objects.filter(school_id=pk, user_id=user_id).exists()

        if not user_count:
            school_user = SchoolUser(school=school, user=user)
            school_user.save()

        return Response({'message': 'Öğretmen okula başarıyla eklendi.'})

    # okuldan öğretmen siler
    def detach_teacher(self, request, pk=None):

        self.get_object()
        relation_id = request.data.get('relation_id')
        manager = SchoolTeacher.objects.get(id=relation_id)
        manager.delete()

        # TODO sınıflarda var ise oralardanda kaydının silinmesi gerekli. Bu problem oluşturmaz.
        # TODO lessonteacher ise ne yapılacak ? Ders silinirse derse ait tüm öğrenci bilgilerinin silinmesi gerekli.
        # TODO lessonteacher ise silinme yapılamalı. Sonuçta derse başka öğretmen ataması yapılacak.

        return Response({'message': 'Öğretmen okuldan başarıyla silindi.'})

    # okula eklenmiş kullanıcıları listeler
    def user_list(self, request, pk=None):
        queryset = School.objects.prefetch_related('user').filter(id=pk).first()
        self.get_object()

        serializer = SchoolUserSerializer(queryset.user.all(), many=True)
        return Response(serializer.data)

    # okula kullanıcı ekler
    def attach_user(self, request, pk=None):
        self.get_object()
        user_id = request.data.get('user_id')

        user_count = SchoolUser.objects.filter(school_id=pk, user_id=user_id).exists()

        if user_count:
            return Response({'error': 'Kullanıcı okula daha önce eklenmiş.'})

        school = School.objects.get(id=pk)
        user = User.objects.get(id=user_id)

        school_user = SchoolUser(school=school, user=user)
        school_user.save()

        return Response({'message': 'Kullanıcı okula başarıyla eklendi.'})

    # okuldan kullanıcı siler
    def detach_user(self, request, pk=None):
        self.get_object()
        relation_id = request.data.get('relation_id')
        user = SchoolUser.objects.get(id=relation_id)

        user_id = user.user_id
        school_id = user.school_id

        SchoolTeacher.objects.filter(teacher_id=user_id, school_id=school_id).delete()
        SchoolStudent.objects.filter(student_id=user_id, school_id=school_id).delete()
        SchoolManager.objects.filter(manager_id=user_id, school_id=school_id).delete()

        # TODO kullanıcı sınıflarda var ise oralardanda kaydının silinmesi gerekli
        # TODO kullanıcı lessonteacher ise ne yapılacak ?

        user.delete()

        return Response({'message': 'Kullanıcı başarıyla silindi.'})

    # kullanıcı rollerini güncellerler
    def update_roles(self, request, pk=None):
        # SIGNAL : Pattern listesine manager için signal ile ekleme yapılıyor
        # SIGNAL : Role listesine manager için signal ile ekleme yapılıyor

        instance = self.get_object()

        roles = request.data.get('roles')
        user_id = request.data.get('id')
        user = User.objects.get(id=user_id)

        user_count = SchoolUser.objects.filter(school_id=pk, user_id=user_id).exists()

        '''
        Kullanıcı daha önce eklenmiş ise rollerini güncelleyelim. 
        Roller güncellenirken ilişkili başka rollere eklenmişmi kontrol edilmeli.
        '''
        if user_count:

            teacher_count = SchoolTeacher.objects.filter(school_id=pk, teacher_id=user_id).exists()
            student_count = SchoolStudent.objects.filter(school_id=pk, student_id=user_id).exists()
            manager_count = SchoolManager.objects.filter(school_id=pk, manager_id=user_id).exists()

            # Daha önceden yönetici rolü eklenmiş ve yeni rollerde yoksa
            if manager_count and 1 not in roles:
                SchoolManager.objects.filter(school_id=pk, manager_id=user_id).delete()

            # Daha önceden öğretmen rolü eklenmiş ve yeni rollerde yoksa
            if teacher_count and 2 not in roles:
                #  Eğer öğretmen derse atanmışsa silinmesini engelleyelim.
                school_teacher = SchoolTeacher.objects.filter(school_id=pk, teacher_id=user_id).first()
                school_lesson_teacher = SchoolLessonTeacher.objects.filter(teacher=school_teacher).exists()

                if school_lesson_teacher:
                    return Response({'error': 'Bu kullanıcı derse atanmış. Öncelikle ders ilişkisini kaldırın.'},
                                    status=status.HTTP_400_BAD_REQUEST)
                else:
                    school_teacher.delete();

            # Daha önceden öğrenci rolü eklenmiş ve yeni rollerde yoksa
            if student_count and 3 not in roles:
                # TODO sınıflara daha önceden eklenmiş mi?
                # TODO Eklendi ise silmeye izin vermeyeceğiz veya tüm bilgisi silinecek.
                SchoolStudent.objects.filter(school_id=pk, student_id=user_id).delete()

            # Yeni rollerin eklemesini yapalım.
            for role in roles:

                if role == 1:
                    if not manager_count:
                        SchoolManager(school=instance, manager=user).save()
                elif role == 2:
                    if not teacher_count:
                        SchoolTeacher(school=instance, teacher=user).save()
                elif role == 3:
                    if not student_count:
                        SchoolStudent(school=instance, student=user).save()

        else:
            SchoolUser(school=instance, user=user).save()
            # Yeni rollerin eklemesini yapalım.
            for role in roles:

                if role == 1:
                    SchoolManager(school=instance, manager=user).save()
                elif role == 2:
                    SchoolTeacher(school=instance, teacher=user).save()
                elif role == 3:
                    SchoolStudent(school=instance, student=user).save()

        return Response({'message': 'Okul rolleri başarıyla eklendi.'})

    # okula atanmış testleri listeler
    def test_list(self, request, pk=None):
        self.get_object()
        queryset = School.objects.prefetch_related('test','test__question').filter(id=pk).first()

        response = []
        for data in queryset.schooltest_set.all():
            response.append({
                'school_test_id': data.id,
                'test_id': data.test.id,
                'test_name': data.test.name,
                'test_question_count': data.test.question.count()
            })
        return Response(response)