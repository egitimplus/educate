from abc import ABC, abstractmethod


class CourseAbstract(ABC):

    @abstractmethod
    def detail(self):
        pass

    @abstractmethod
    def component_stats(self):
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
