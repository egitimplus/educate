from abc import ABC, abstractmethod


class CourseAbstract(ABC):

    @abstractmethod
    def detail(self):
        pass

    @abstractmethod
    def stat(self):
        pass

    @abstractmethod
    def lesson(self):
        pass

    @abstractmethod
    def unit(self):
        pass

    @abstractmethod
    def lecture_stat(self):
        pass
