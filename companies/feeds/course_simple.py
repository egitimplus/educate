from companies.feeds import CourseAbstract


class CourseSimpleRepository(CourseAbstract):

    def __init__(self, **kwargs):
        self.__parent = kwargs.pop("parent", None)

    def detail(self):
        pass

    def lesson(self):
        pass

    def stat(self):
        pass

    def unit(self):
        pass

    def lecture_stat(self):
        pass
