from rest_framework import viewsets, mixins
from publishers.models import Book, Source
from questions.models import Question
from publishers.serializers import SourceSerializer, BookSerializer
from questions.serializers import QuestionSerializer
from library.serializers import ExamSerializer
from educategories.serializers import EduCategorySerializer
from rest_framework.response import Response


class BookViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def question_list(self, request, pk=None):
        queryset = Question.objects.filter(book_id=pk).all()
        self.get_object()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = QuestionSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)


    # kitaba bağlı kaynak listesi
    def source_list(self, request, pk=None):
        queryset = Source.objects.filter(book_id=pk, parent=None).all()
        self.get_object()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = SourceSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SourceSerializer(queryset, many=True)
        return Response(serializer.data)

    def exam_list(self, request, pk=None):
        instance = self.get_object()
        exams = instance.exam.all()

        serializer = ExamSerializer(exams, many=True)

        return Response(serializer.data)

    def attach_exam(self, request, pk=None):
        instance = self.get_object()
        exam_id = request.data.get('id')

        instance.exam.add(exam_id)

        return Response({'message': 'Sınav kitaba eklendi.'})

    def detach_exam(self, request, pk=None):
        instance = self.get_object()
        exam_id = request.data.get('id')

        instance.exam.remove(exam_id)

        return Response({'message': 'Sınav kitaptan silindi.'})

    def lesson_list(self, request, pk=None):
        instance = self.get_object()
        lessons = instance.lesson.all()

        serializer = EduCategorySerializer(lessons, many=True)

        return Response(serializer.data)

    def attach_lesson(self, request, pk=None):
        instance = self.get_object()
        lesson_id = request.data.get('id')

        instance.lesson.add(lesson_id)

        return Response({'message': 'Ders kitaba eklendi.'})

    def detach_lesson(self, request, pk=None):
        instance = self.get_object()
        lesson_id = request.data.get('id')

        instance.lesson.remove(lesson_id)

        return Response({'message': 'Ders kitaptan silindi.'})
