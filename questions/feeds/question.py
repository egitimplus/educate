from questions.models import QuestionAnswerStat, QuestionUnique
from components.feeds import ComponentMixin
from questions.feeds import QuestionStatRepository, QuestionAnswerRepository, QuestionUniqueRepository
from library.mixins import TestUniqueMixin, RequestMixin


class QuestionRepository(TestUniqueMixin, RequestMixin, ComponentMixin):
    __components = None
    __code = None
    __true_answer = None
    __stat = None
    __answer = None
    __unique = None
    __object = None
    __request = None

    def __init__(self, **kwargs):
        self.__object = kwargs.pop("question", None)

    def create_stat(self):
        self.__stat = QuestionStatRepository(question=self)

    def create_answer(self, question_answer=None):
        self.__answer = QuestionAnswerRepository(question=self, question_answer=question_answer)

    def create_unique(self):
        obj, created = QuestionUnique.objects.get_or_create(question_code=self.__code)
        self.__unique = QuestionUniqueRepository(question=self, question_unique=obj)

    def set_components(self):
        self.__components = self.__object.component.all()

    def set_true_answer(self):
        self.__true_answer = self.__object.true_answer

    def set_code(self):
        self.__code = self.__object.code

    @property
    def true_answer(self):
        return self.__true_answer

    @property
    def components(self):
        return self.__components

    @property
    def answer(self):
        return self.__answer

    @property
    def stat(self):
        return self.__stat

    @property
    def unique(self):
        return self.__unique

    @property
    def object(self):
        return self.__object

    # kullanıcılar soruyu daha önce çözmüş mü ?
    def have_answer_stat(self):
        have_answer = QuestionAnswerStat.objects.filter(question=self.__object, user=self.__request.user).exists()
        if have_answer:
            return True

        return False

