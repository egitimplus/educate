from questions.models import QuestionAnswerStat, QuestionUnique, QuestionUniqueStat
from components.feeds import ComponentMixin
from questions.feeds import QuestionStatRepository, QuestionAnswerRepository, QuestionUniqueRepository


class QuestionRepository(ComponentMixin):

    def __init__(self, request, **kwargs):

        self.queryset = kwargs.pop("question", None)
        self.test_unique = kwargs.pop("test_unique", None)
        self.request = request
        self.components = None
        self.code = None
        self.true_answer = None
        self.test_unique = None

    def prepare_question(self):
        self.set_components()
        self.set_code()
        self.set_true_answer()

    def set_components(self):
        self.components = self.queryset.component.all()

    def set_true_answer(self):
        self.true_answer = self.queryset.answers.filter(is_true_answer=1).first()

    def set_code(self):
        unique = sorted(set(self.components.values_list('id', flat=True)))

        self.code = '-'.join(map(str, unique))

    def stat(self):
        return QuestionStatRepository(
            request=self.request,
            question=self.queryset,
            test_unique=self.test_unique,
        )

    def answer(self):
        return QuestionAnswerRepository(
            request=self.request,
            question=self.queryset,
            test_unique=self.test_unique,
        )

    def unique(self):
        obj, created = QuestionUnique.objects.get_or_create(question_code=self.code)
        return QuestionUniqueRepository(
            request=self.request,
            question=self.queryset,
            test_unique=self.test_unique,
            question_unique=obj
        )

    # kullanıcılar soruyu daha önce çözmüş mü ?
    def have_answer_stat(self):
        have_answer = QuestionAnswerStat.objects.filter(question=self.queryset).exists()
        if have_answer:
            return True

        return False

