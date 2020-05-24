from tests.models import TestUnique
import math
from library.feeds import flatten, search_id
from questions.feeds import QuestionRepository
from components.models import ComponentAnswer
from components.feeds import ComponentStatRepository


class TestAnswerRepository:

    def __init__(self, request, test):
        self._request = request
        self._queryset = test
        self._test_unique = None

        self._true = 0
        self._false = 0
        self._empty = 0
        self._total = 0

        self._true_components = []
        self._false_components = []
        self._empty_components = []

        self._answers = None
        self._component_stats = None

        self.set_test_unique()

    @property
    def answers(self):
        return self._answers

    @answers.setter
    def answers(self, value):
        self._answers = value

    @property
    def component_stats(self):
        return self._component_stats

    @component_stats.setter
    def component_stats(self, value):
        self._component_stats = value

    def set_test_unique(self):
        test_unique = TestUnique.objects.create(
            user_id=self._request.user.id,
            test_id=self._queryset.id,
            report='report',
            test_result=0
        )

        self._test_unique = test_unique

    def test_result(self):
        result = math.ceil((self._true / self._total) * 100)

        if result > 100:
            result = 100

        return result

    def all_components(self):
        all_components = self._true_components + self._false_components + self._empty_components

        return list(set(flatten(all_components)))

    def update_component_status(self, component_id):

        true_component_diff = 10
        false_component_diff = 20
        true_component_percent = 50

        component_status = search_id(component_id, self._component_stats)

        data = {'status': 0, 'percent': 0, 'repeat': 0, 'solved': 1}

        if component_status:
            data['status'] = component_status.status
            data['percent'] = component_status.percent
            data['repeat'] = component_status.repeat
            data['solved'] = component_status.solved + 1

        true_count = self._true_components.count(component_id)
        false_count = self._false_components.count(component_id)

        stat_count = true_count - false_count
        answer_is_true = 1 if stat_count > 0 else 0

        if answer_is_true == 1:
            for i in range(0, stat_count):
                data['repeat'] = data['repeat'] + 1 + i if data['repeat'] > 0 else 1
                data['percent'] = data['percent'] + true_component_diff if data['percent'] > 40 else 50
        else:
            for i in range(0, stat_count):
                data['repeat'] = data['repeat'] + i + 1 if data['repeat'] < 0 else -1
                data['percent'] = data['percent'] - (data['repeat'] * false_component_diff)

            if data['percent'] < 0:
                data['percent'] = 0

        new_status = 1 if data['percent'] >= true_component_percent else 0

        self.status_change_add(data['status'], new_status)

        return data

    def status_change_add(self, old, new):
        pass

    def finish(self):
        questions = self._queryset.questions()

        self._total = len(questions)

        for question in questions:
            qr = QuestionRepository(request=self._request, question=question, test_unique=self._test_unique)
            qr.prepare_question()

            qs = qr.stat()
            qa = qr.answer()

            i = 0

            # post edilen soru cevaplarına göre veri tabanında gerekli düzenlemeleri yapalım
            for answer in self.answers:
                qa.answer_id = answer['question_id']
                # Eğer post edilen cevaplar içerisinde bu soru için cevap bulunduysa
                if qa.answer_id == question.id:
                    i = i + 1
                    # Eğer post edilen cevap doğru ise
                    if qa.answer_id == qr.true_answer.id:

                        self._true_components.append(qs.add_true())
                        self._true = self._true + 1

                        # cevabı soru istatistiklerine ekleyelim
                        qa.answer_is_true = 1
                        qa.add_answer()

                    # Eğer post edilen cevap yanlış ise
                    else:
                        component_answers = ComponentAnswer.objects.select_related(
                            'component'
                        ).filter(question_answer_id=qa.answer_id).all()

                        if len(component_answers) > 0:
                            # sorudaki soru parçaları için gerekli işlemleri yapalım

                            for component_answer in component_answers:
                                csr = ComponentStatRepository(
                                    request=self._request,
                                    component=component_answer.component,
                                    question=question,
                                    test_unique=self._test_unique
                                )

                                if component_answer.component_ok == 1:
                                    # soru parçasını doğru soru parçası listesine ekleyelim

                                    self._true_components.append(csr.add_true_answer())

                                else:
                                    # soru parçasını yanlış soru parçası listesine ekleyelim
                                    self._false_components.append(csr.add_false_answer())
                        else:
                            # soru parçasını yanlış soru parçası listesine ekleyelim
                            self._false_components.append(qs.add_false())

                        self._false = self._false + 1
                        qa.answer_is_true = 0
                        # cevabı soru istatistiklerine ekleyelim
                        qa.add_answer()

            # Eğer post edilen cevaplar içerisinde bu soru için cevap bulunamadıysa
            if i == 0:
                # soru parçasını boş soru parçası listesine ekleyelim
                self._empty_components.append(qs.add_empty())
                # boş soru sayısını bir artıralım
                self._empty = self._empty + 1
            # question unique oluşturularım ve istatistikleri ekleyelim
            qu = qr.unique()
            qu.update_stats(qa.answer_is_true)
