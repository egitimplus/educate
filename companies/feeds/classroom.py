from library.mixins import RequestMixin


class ClassroomRepository(RequestMixin):

    def __init__(self, **kwargs):
        self._object = kwargs.pop("classroom", None)

    @property
    def teachers(self):
        return self._object.teacher.all()

    @property
    def students(self):
        return self._object.student.all()

    def attach_student(self):
        # SIGNAL : Pattern listesine signal ile ekleme yapılıyor
        # SIGNAL : Role listesine signal ile ekleme yapılıyor

        users = self._request.data.get('users')
        school = self._object.school

        for user in users:
            if school.user.filter(student_id=user).exists():
                if not self._object.filter(student_id=user).exists():
                    self._object.student.add(user)


