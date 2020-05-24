
class ClassroomRepository:

    def __init__(self, request, classroom):
        self._request = request
        self._queryset = classroom

    def teacher_ids(self):
        return self._queryset.teacher.all().values_list('id', flat=True)




