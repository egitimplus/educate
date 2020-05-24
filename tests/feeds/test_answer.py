from tests.models import TestUnique
import math
from library.feeds import flatten, search_id
from questions.feeds import QuestionRepository
from components.models import ComponentStat, ComponentAnswer
from components.feeds import ComponentStatRepository


class TestAnswerRepository:

    def __init__(self, request, test):
        self.request = request
        self.queryset = test
        self.counts = {'true': 0, 'false': 0, 'empty': 0, 'total': 0}
        self.components = {'true': [], 'false': [], 'empty': []}
        self.answers = None
        self.component_stats = None
        self.test_unique = None

        self.set_test_unique()

    def set_answers(self, answers):
        self.answers = answers

    def set_counts(self, answer_type, count):
        self.counts[answer_type] = self.counts[answer_type] + count

    def set_component(self, answer_type, components):
        self.components[answer_type].append(components)

    def set_component_stats(self, component_stats):
        self.component_stats = component_stats

    def set_test_unique(self):
        test_unique = TestUnique.objects.create(
            user_id=self.request.user.id,
            test_id=self.queryset.id,
            report='report',
            test_result=0
        )

        self.test_unique = test_unique

    def test_result(self):
        result = math.ceil((self.counts['true'] / self.counts['total']) * 100)

        if result > 100:
            result = 100

        return result

    def all_components(self):
        all_components = self.components['true'] + self.components['false'] + self.components['empty']

        return list(set(flatten(all_components)))

    def update_component_status(self, component_id):

        true_component_diff = 10
        false_component_diff = 20
        true_component_percent = 50

        component_status = search_id(component_id, self.stats)

        data = {'status': 0, 'percent': 0, 'repeat': 0, 'solved': 1}

        if component_status:
            data['status'] = component_status.status
            data['percent'] = component_status.percent
            data['repeat'] = component_status.repeat
            data['solved'] = component_status.solved + 1

        true_count = self.components['true'].count(component_id)
        false_count = self.components['false'].count(component_id)

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
        questions = self.queryset.questions()

        self.set_counts('total', len(questions))

        for question in questions:
            qr = QuestionRepository(request=self.request, question=question, test_unique=self.test_unique)
            qr.prepare_question()

            qs = qr.stat()
            qa = qr.answer()

            i = 0

            # post edilen soru cevaplarına göre veri tabanında gerekli düzenlemeleri yapalım
            for answer in self.answers:
                qa.set_answer_id(answer['question_id'])
                # Eğer post edilen cevaplar içerisinde bu soru için cevap bulunduysa
                if qa.answer_id == question.id:
                    i = i + 1
                    # Eğer post edilen cevap doğru ise
                    if qa.answer_id == qr.true_answer.id:
                        self.set_component('true', qs.add_true())
                        self.set_counts('true', 1)

                        # cevabı soru istatistiklerine ekleyelim
                        qa.set_answer_is_true(1)
                        qa.add_answer()

                    # Eğer post edilen cevap yanlış ise
                    else:
                        component_answers = ComponentAnswer.objects.select_related(
                            'component'
                        ).filter(question_answer_id=answer['answer_id']).all()

                        if len(component_answers) > 0:
                            # sorudaki soru parçaları için gerekli işlemleri yapalım

                            for component_answer in component_answers:
                                csr = ComponentStatRepository(
                                    request=self.request,
                                    component=component_answer.component,
                                    question=question,
                                    test_unique=self.test_unique
                                )

                                if component_answer.component_ok == 1:
                                    # soru parçasını doğru soru parçası listesine ekleyelim
                                    self.set_component('true', csr.add_true_answer())

                                else:
                                    # soru parçasını yanlış soru parçası listesine ekleyelim
                                    self.set_component('false', csr.add_false_answer())

                        else:
                            # soru parçasını yanlış soru parçası listesine ekleyelim
                            self.set_component('false', qs.add_false())

                        self.set_counts('false', 1)

                        qa.set_answer_is_true(0)
                        # cevabı soru istatistiklerine ekleyelim
                        qa.add_answer()

            # Eğer post edilen cevaplar içerisinde bu soru için cevap bulunamadıysa
            if i == 0:
                # soru parçasını boş soru parçası listesine ekleyelim
                self.set_component('empty', qs.add_empty())

                # boş soru sayısını bir artıralım
                self.set_counts('empty', 1)
            # question unique oluşturularım ve istatistikleri ekleyelim
            qu = qr.unique()
            qu.update_stats(qa.answer_is_true)
