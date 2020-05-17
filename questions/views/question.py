from django.db import transaction
from django.http import Http404
from rest_framework import status, viewsets, mixins, views
from rest_framework.response import Response
from rest_framework.decorators import action
from questions.serializers import QuestionSerializer, QuestionPostSerializer
from publishers.serializers import SourceQuestionSerializer
from questions.models import Question, QuestionExam
from components.feeds import ComponentPartRepository
from components.models import ComponentAnswer
from library.feeds import get_breadcrumb, get_category, send_question_change_message_to_users as send_message


class QuestionViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    Question Methods - list, retrieve, crate, update, destroy
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Soru ayrıntıları
        TODO File, Domain, Path eklenecek.
        """
        pk = self.kwargs['pk']

        queryset = Question.objects.filter(id=pk).prefetch_related(
            'question_answers',
            'edu_category'
        ).first()

        serialized_question = QuestionSerializer(queryset)

        response = serialized_question.data
        response.update(
            {
                'category':  get_category(queryset.edu_category_id),
                'breadcrumb': get_breadcrumb(queryset.edu_category_id)
            }
        )

        return Response(response)

    @action(methods=['GET'], detail=True)
    def parents(self, request, pk=None):
        question = Question.objects.values_list('edu_category_id', flat=True).filter(id=pk).first()

        categories = get_breadcrumb(question)
        return Response(categories)

    @action(methods=['GET'], detail=True)
    def user_detail(self, request, pk=None):
        """
        Soru ayrıntılarını kullanıcı istatistikleri ile birlikte döndürür.
        all_components, breadcrumb
        """
        queryset = Question.objects.filter(id=pk).prefetch_related(
            'component',
            'component__source_component',
            'question_answers'
        ).first()

        serialized_question = QuestionSerializer(queryset)

        question_repo = ComponentPartRepository(request=request, question=queryset)

        all_components = question_repo.all_components()

        response = serialized_question.data
        response.update({
            'components': all_components['components'],
            'all_components': all_components['all_components'],
            'category':  get_category(queryset.edu_category_id),
            'breadcrumb':  get_breadcrumb(queryset.edu_category_id)
        })

        return Response(response)

    @action(methods=['GET'], detail=True)
    def view(self, request, pk=None):
        queryset = Question.objects.filter(id=pk).prefetch_related(
            'component',
            'component__source_component',
            'question_answers',
            'question_answers__component',
            'exam'
        ).first()

        question_repo = ComponentPartRepository(request, queryset)

        source = SourceQuestionSerializer(queryset.source_questions, many=True)

        answers = []
        for answer in queryset.question_answers.all():
            component_answers = ComponentAnswer.objects.filter(question_answer_id=answer.id).all()

            component_answer_check = []
            for component_answer in component_answers:
                component_answer_check.append({
                    'id': component_answer.id,
                    'component_id': component_answer.component_id,
                    'component_ok': component_answer.component_ok
                })

            repo = ComponentPartRepository(request, answer)

            answer_data = {
                'id': answer.id,
                'answer_type': answer.answer_type,
                'answer_value': answer.answer_value,
                'answer_choice': answer.answer_choice,
                'is_true_answer': answer.is_true_answer,
                'components': {
                    'component_answer_check': component_answer_check,
                    'all_sub_components': repo.all_sub_components(return_format='list'),
                    'sub_components': repo.sub_components(return_format='list'),
                    'data_components': repo.sub_components()
                }
            }
            answers.append(answer_data)

        exam = QuestionExam.objects.select_related('exam').filter(question_id=pk).all()

        exams = []
        for item in exam:
            exams.append({
                'id': item.id,
                'exam_name': item.exam.name,
                'exam_year': item.exam_year,
                'exam_id': item.exam_id
            });

        response = {
            'id': queryset.id,
            'name': queryset.name,
            'level': queryset.level,
            'question_start_type': queryset.question_start_type,
            'question_start_value': queryset.question_start_value,
            'question_answer_type': queryset.question_answer_type,
            'question_answer_value': queryset.question_answer_value,
            'question_pattern': queryset.question_pattern,
            'active': queryset.active,
            'seconds': queryset.seconds,
            'source_questions': source.data,
            'exam': exams,
            'question_answers': answers,
            'all_sub_components':  question_repo.all_sub_components(return_format='list'),
            'sub_components': question_repo.sub_components(return_format='list'),
            'data_components': question_repo.data_sub_components(),
            'all_data_components': question_repo.data_all_sub_components(),
            'category': get_category(queryset.edu_category_id),
            'breadcrumb': get_breadcrumb(queryset.edu_category_id)
        }

        return Response(response)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = QuestionPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.save()
        return Response(question, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = QuestionPostSerializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response([])

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        question_repo = ComponentPartRepository(request, instance)

        if question_repo.have_answer_stat():
            # TODO sadece soruyu pasifleştirme yeterli mi ? Bunun üzerine düşünmek gerekli.
            # soru daha önce çözülmüş silinme yapılamaz. pasifleştirme yapalım.
            # question modelinin pre_save methodunda güncelleme mesajı gönderiyor.
            # burada save() methodu kullanmayarak bu mesajı göndermekten kaçınalım.
            # messajı burada kendimiz gönderelim.
            instance.update(active=0)
            send_message(instance, type='disable')
            pass
        else:
            # soru daha önce çözülmemiş silinebilir.
            instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['POST'], detail=False)
    def search(self, request):
        search_text = request.data.get('search_text', None)

        queryset = Question.objects.values_list('id').filter(name__icontains=search_text)

        ids = []
        for question in queryset:
            ids.append(question[0])

        return Response(ids)


class CategoryView(views.APIView):
    """
    Kategoriye bağlı soru listesi (sadece soru ID leri)
    """
    def get_object(self, pk):
        try:
            return Question.objects.values_list('id').filter(edu_category_id=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        questions = self.get_object(pk)
        ids = []
        for question in questions:
            ids.append(question[0])

        return Response(ids)
