from questions.models import QuestionAnswerStat, QuestionUnique, QuestionUniqueStat
from components.feeds import ComponentMixin
from questions.feeds import QuestionStatRepository, QuestionAnswerRepository, QuestionUniqueRepository


class QuestionRepository(ComponentMixin):

    def __init__(self, request, **kwargs):

        self._queryset = kwargs.pop("question", None)
        self._test_unique = kwargs.pop("test_unique", None)
        self._request = request
        self._components = None
        self._code = None
        self._true_answer = None

    def prepare_question(self):
        self.set_components()
        self.set_code()
        self.set_true_answer()

    def set_components(self):
        self._components = self._queryset.component.all()

    def set_true_answer(self):
        self._true_answer = self._queryset.answers.filter(is_true_answer=1).first()

    def set_code(self):
        unique = sorted(set(self._components.values_list('id', flat=True)))

        self._code = '-'.join(map(str, unique))

    @property
    def true_answer(self):
        return self._true_answer

    def stat(self):
        return QuestionStatRepository(
            request=self._request,
            question=self._queryset,
            components=self._components,
            test_unique=self._test_unique,
        )

    def answer(self):
        return QuestionAnswerRepository(
            request=self._request,
            question=self._queryset,
            test_unique=self._test_unique,
        )

    def unique(self):
        obj, created = QuestionUnique.objects.get_or_create(question_code=self._code)
        return QuestionUniqueRepository(
            request=self._request,
            question=self._queryset,
            test_unique=self._test_unique,
            question_unique=obj
        )

    # kullanıcılar soruyu daha önce çözmüş mü ?
    def have_answer_stat(self):
        have_answer = QuestionAnswerStat.objects.filter(question=self._queryset).exists()
        if have_answer:
            return True

        return False

