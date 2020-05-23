from rest_framework import viewsets, mixins, status
from companies.models import ClassroomStudent, ClassroomLesson, Lesson
from curricula.models import LearningLesson, LearningUnit
from curricula.serializers import LearningLessonSerializer, LearningUnitSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
#import query_debugger


class LearningLessonViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                            mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = LearningLesson.objects.all()
    serializer_class = LearningLessonSerializer

    # derse bağlı unit listesi
    @action(methods=['GET'], detail=True)
    def unit_list(self, request, pk=None):

        curricula = LearningLesson.objects.filter(id=pk).first()

        queryset = LearningUnit.objects.filter(lesson_id=curricula.id).all()

        serializer = LearningUnitSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

    # kullanıcı ders listesi
    @action(methods=['GET'], detail=False)
    def info(self, request):

        #user_id = request.user.id
        #classroom_id = int(request.query_params.get('classroom'))

        user_id = 3
        classroom_id = 101

        queryset = ClassroomStudent.objects.filter(student_id=user_id, classroom_id=classroom_id).first()

        if queryset:
            data = []
            lesson_queryset = ClassroomLesson.objects.prefetch_related(
                'lesson__lesson__curricula__units__subjects').filter(
                classroom_id=classroom_id,
                lesson__lesson__curricula__public=1,
                lesson__lesson__curricula__unit__id=1001
            ).all()


            """
            SELECT 
                `companies_classroom_lesson`.`id`, 
                `companies_classroom_lesson`.`lesson_id`, 
                `companies_classroom_lesson`.`classroom_id`
            FROM 
                `companies_classroom_lesson` 
            INNER JOIN 
                `companies_school_lesson_teacher` 
                ON (`companies_classroom_lesson`.`lesson_id` = `companies_school_lesson_teacher`.`id`) 
            INNER JOIN 
                `companies_lesson` 
                ON (`companies_school_lesson_teacher`.`lesson_id` = `companies_lesson`.`id`) 
            INNER JOIN `curricula_learning_lesson` 
                ON (`companies_lesson`.`curricula_id` = `curricula_learning_lesson`.`id`) 
            INNER JOIN `curricula_learning_unit` ON (`curricula_learning_lesson`.`id` = `curricula_learning_unit`.`lesson_id`) 
            
            WHERE (
            `companies_classroom_lesson`.`classroom_id` = 101 AND 
            `curricula_learning_lesson`.`public` = 1 AND 
            `curricula_learning_unit`.`id` = 1001
            )
             """
           

            for x in lesson_queryset:

                unit_serializer = LearningUnitSerializer(x.lesson.lesson.curricula.units.order_by('position').all(), many=True, context={'request': request})
                data.append({
                    'id': x.id,
                    'school': {
                        'id': x.lesson.lesson.school_id,
                        'lesson_id': x.lesson.lesson.id,
                        'lesson_name': x.lesson.lesson.name
                    },
                    'class': {
                        'id': x.classroom_id,
                        'lesson_id': x.lesson.id,
                        'lesson_name': x.lesson.name,
                        'duration': x.lesson.duration,
                        'teacher_id': x.lesson.teacher_id
                    },
                    'curricula': {
                        'id': x.lesson.lesson.curricula.id,
                        'name': x.lesson.lesson.curricula.name,
                        'units': unit_serializer.data
                    },
                })


            return Response(data)



        return Response({'error': 'Sınıf öğrencisi bulunamadı.'}, status=status.HTTP_400_BAD_REQUEST)

    # ders görüntüleme
    @action(methods=['GET'], detail=True)
    def user_view(self, request, pk=None):

        queryset = ClassroomLesson.objects.prefetch_related(
            'lesson__lesson__curricula__units__subjects'
        ).filter(id=pk).first()

        if queryset:

            unit_serializer = LearningUnitSerializer(
                queryset.lesson.lesson.curricula.units.order_by('position').all(), many=True, context={'request': request})

            data = {
                'school': {
                    'id': queryset.lesson.lesson.school_id,
                    'lesson_id': queryset.lesson.lesson.id,
                    'lesson_name': queryset.lesson.lesson.name
                },
                'class': {
                    'id': queryset.classroom_id,
                    'lesson_id': queryset.lesson.id,
                    'lesson_name': queryset.lesson.name,
                    'duration': queryset.lesson.duration,
                    'teacher_id': queryset.lesson.teacher_id
                },
                'curricula': {
                    'id': queryset.lesson.lesson.curricula.id,
                    'name': queryset.lesson.lesson.curricula.name,
                    'units': unit_serializer.data
                },
            }

            return Response(data)

        return Response('Ders bulunamadı.', status=status.HTTP_400_BAD_REQUEST)
