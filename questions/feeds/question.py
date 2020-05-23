from questions.models import QuestionAnswerStat, QuestionUnique, QuestionUniqueStat
from components.feeds import ComponentStatRepository, ComponentMixin


class QuestionRepository(ComponentMixin):

    def __init__(self, request, question, prepare=False):
        self.request = request
        self.queryset = question
        self.components = None
        self.code = None
        self.true_answer = None

        if prepare:
            self.prepare_question()

    def prepare_question(self):
        self.components = self.get_components()
        self.code = self.create_unique()
        self.true_answer = self.get_true_answer()

    def get_components(self):
        return self.queryset.component.all()

    def get_true_answer(self):
        return self.queryset.answers.filter(is_true_answer=1).first()

    def create_unique(self):
        if self.components is None:
            self.prepare_answer()

        unique = sorted(set(self.components.values_list('id', flat=True)))

        return '-'.join(map(str, unique))

    def add_true_answer(self, **kwargs):
        test_unique = kwargs.pop("test_unique", None)
        c = list()

        for component in self.components:

            csr = ComponentStatRepository(request=self.request, component=component)

            true_components = csr.add_true_answer(question=self.queryset, test_unique=test_unique,)
            c.append(component.id)

            for tc in true_components:
                c.append(tc)

        return c

    def add_false_answer(self, **kwargs):
        test_unique = kwargs.pop("test_unique", None)
        c = list()

        for component in self.components:

            csr = ComponentStatRepository(
                request=self.request,
                component=component
            )

            csr.add_false_answer(
                question=self.queryset,
                test_unique=test_unique,
            )

            # soru parçasını doğru soru parçası listesine ekleyelim
            c.append(component.id)

        return c

    def add_empty_answer(self, **kwargs):
        test_unique = kwargs.pop("test_unique", None)
        c = list()

        for component in self.components:

            csr = ComponentStatRepository(
                request=self.request,
                component=component
            )

            csr.add_empty_answer(
                question=self.queryset,
                test_unique=test_unique,
            )

            # soru parçasını doğru soru parçası listesine ekleyelim
            c.append(component.id)

        return c

    def add_question_answer(self, **kwargs):
        answer_is_true = kwargs.pop("answer_is_true", None)
        question_answer_id = kwargs.pop("question_answer_id", None)
        test_unique = kwargs.pop("test_unique", None)

        # cevabı soru istatistiklerine ekleyelim
        QuestionAnswerStat.objects.create(
            answer_is_true=answer_is_true,
            answer_seconds=0,
            answer_type=1,
            question=self.queryset,
            user=self.request.user,
            test_unique=test_unique,
            question_answer_id=question_answer_id,
            answer_count=1
        )

    def create_question_unique(self, answer_is_true):

        if self.code is None:
            self.prepare_question()

        # soru unique kodunu veritabanında varsa güncelleyelim eğer yoksa ekleyelim
        obj, created = QuestionUnique.objects.get_or_create(question_code=self.code)

        question_unique_stat = QuestionUniqueStat.objects.filter(question_code=self.code).first()

        # verilen cevaba göre soru için yeni bir kod oluşturalım
        question_unique = self.question_unique_status(question_unique_stat, answer_is_true)

        # unique soru istatistiklerini ekleyelim
        QuestionUniqueStat.objects.update_or_create(
            question_unique_id=obj.id,
            user=self.request.user,
            question_code=self.code,
            defaults={
                "status": question_unique['status'],
                "percent": question_unique['percent'],
                "solved": question_unique['solved'],
                "repeat": question_unique['repeat'],
            }
        )

    # kullanıcılar soruyu daha önce çözmüş mü ?
    def have_answer_stat(self):
        have_answer = QuestionAnswerStat.objects.filter(question=self.queryset).exists()
        if have_answer:
            return True

        return False

    """
    " Puan Hesaplama Kuralları
    " -------------------------------------
    " 
    """
    def question_unique_status(self, question_unique_stat, answer_is_true):

        true_question_diff = 10
        false_question_diff = 20
        true_question_percent = 50

        repeat = 0
        percent = 0
        solved = 1

        if question_unique_stat:
            repeat = question_unique_stat.repeat
            percent = question_unique_stat.percent
            solved = question_unique_stat.solved + 1

        if answer_is_true == 1:
            repeat = repeat + 1 if repeat > 0 else 1
            percent = percent + true_question_diff if percent > 40 else 50
        else:
            repeat = repeat - 1 if repeat < 0 else -1
            percent = percent - (repeat * false_question_diff)
            if percent < 0:
                percent = 0

        status = 1 if percent >= true_question_percent else 0

        return {
            'status': status,
            'percent': percent,
            'solved': solved,
            'repeat': repeat
        }
