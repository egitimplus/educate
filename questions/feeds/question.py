from questions.models import QuestionAnswerStat, QuestionUnique
from components.feeds import ComponentMixin
from questions.feeds import QuestionStatRepository, QuestionAnswerRepository, QuestionUniqueRepository
from library.mixins import TestUniqueMixin, RequestMixin


class QuestionRepository(TestUniqueMixin, RequestMixin, ComponentMixin):
    _components = None
    _code = None
    _true_answer = None
    _stat = None
    _answer = None
    _unique = None

    def __init__(self, **kwargs):
        self._queryset = kwargs.pop("question", None)

    def create_stat(self):
        self._stat = QuestionStatRepository(question=self)

    def create_answer(self, question_answer=None):
        self._answer = QuestionAnswerRepository(question=self, question_answer=question_answer)

    def create_unique(self):
        obj, created = QuestionUnique.objects.get_or_create(question_code=self._code)
        self._unique = QuestionUniqueRepository(question=self, question_unique=obj)

    def set_components(self):
        self._components = self._queryset.component.all()

    def set_true_answer(self):
        self._true_answer = self._queryset.true_answer

    def set_code(self):
        self._code = self._queryset.code

    @property
    def true_answer(self):
        return self._true_answer

    @property
    def components(self):
        return self._components

    @property
    def answer(self):
        return self._answer

    @property
    def stat(self):
        return self._stat

    @property
    def unique(self):
        return self._unique

    @property
    def queryset(self):
        return self._queryset

    # kullanıcılar soruyu daha önce çözmüş mü ?
    def have_answer_stat(self):
        have_answer = QuestionAnswerStat.objects.filter(question=self._queryset, user=self._request.user).exists()
        if have_answer:
            return True

        return False

