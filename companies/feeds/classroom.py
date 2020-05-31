

class ClassroomRepository:

    def __init__(self, **kwargs):
        self.__object = kwargs.pop("classroom", None)

    @property
    def teachers(self):
        return self.__object.teacher.all()

    @property
    def students(self):
        return self.__object.student.all()

    def attach_student(self):
        # SIGNAL : Pattern listesine signal ile ekleme yapılıyor
        # SIGNAL : Role listesine signal ile ekleme yapılıyor

        users = self.__request.data.get('users')
        school = self.__object.school

        for user in users:
            if school.user.filter(student_id=user).exists():
                if not self.__object.filter(student_id=user).exists():
                    self.__object.student.add(user)


