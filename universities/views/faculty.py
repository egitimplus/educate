from universities.serializers.faculty import *
from rest_framework import generics
from rest_framework.response import Response
from universities.models.faculty import Faculty
from django.db.models import Q


class FacultyList(generics.ListCreateAPIView):

    serializer_class = FacultySerializer

    def get_queryset(self):

        query = Q(title='hukuk')
        query.add(Q(slug='mark@test.com'), Q.OR)
        query.add(Q(province='1'), Q.AND)

        queryset = Faculty.objects.all()

        faculty_id = self.request.query_params.get('id', None)
        if faculty_id is not None:
            queryset = queryset.filter(id=faculty_id)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = FacultySerializer(queryset, many=True, nest=2)
        return Response(serializer.data)