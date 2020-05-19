
class ClassroomRepository:

    def __init__(self, request, classroom):
        self.request = request
        self.queryset = classroom

    def teacher_ids(self):
        return self.queryset.teacher.all().values_list('id', flat=True)




