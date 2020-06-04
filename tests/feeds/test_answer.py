from tests.models import TestUnique
import math
from library.feeds import flatten, search_id
from questions.feeds import QuestionRepository
from questions.models import QuestionAnswer
from components.models import ComponentAnswer, ComponentStatusChange
from components.feeds import ComponentRepository
from library.mixins import TestUniqueMixin, RequestMixin
from components.models import ComponentStat


class TestAnswerRepository(TestUniqueMixin, RequestMixin):

    def __init__(self, **kwargs):
        self.__test = kwargs.pop("test", None)
        self.__test_unique = self.__test.test_unique
        self.__request = self.__test.request
        self.__true = 0
        self.__false = 0
        self.__empty = 0
        self.__total = 0
        self.__true_components = []
        self.__false_components = []
        self.__empty_components = []
        self.__answers = None
        self.__component_stats = None
        self.__all_components = None

    @property
    def answers(self):
        return self.__answers

    @answers.setter
    def answers(self, value):
        self.__answers = value

    @property
    def test_result(self):
        result = math.ceil((self.__true / self.__total) * 100)

        if result > 100:
            result = 100

        return result

    def set_component_stats(self):
        component_stats = ComponentStat.objects.filter(
            component_id__in=self.__all_components,
            user=self.__request.user
        ).values('id', 'component_id', 'component_status')

        self.__component_stats = component_stats

    def set_all_components(self):
        all_components = self.__true_components + self.__false_components + self.__empty_components

        self.__all_components = list(set(flatten(all_components)))

    def update_component_status(self, component_id):

        true_component_diff = 10
        false_component_diff = 20
        true_component_percent = 50

        component_status = search_id(component_id, self.__component_stats)

        data = {'status': 0, 'percent': 0, 'repeat': 0, 'solved': 1}

        if component_status:
            data['status'] = component_status.status
            data['percent'] = component_status.percent
            data['repeat'] = component_status.repeat
            data['solved'] = component_status.solved + 1

        true_count = self.__true_components.count(component_id)
        false_count = self.__false_components.count(component_id)

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

        self.status_change_add(component_id, data['status'], new_status)

        return data

    def status_change_add(self, component_id, old, new):

        ComponentStatusChange.objects.update_or_create(
            component_id=component_id,
            user=self.__request.user,
            defaults={
                "old_status": old,
                "new_status": new
            }
        )

    def set_test_unique(self):
        test_unique = TestUnique.objects.create(
            user_id=self.__request.user.id,
            test_id=self.__test.object.id,
            report='report',
            test_result=0
        )

        self.__test_unique = test_unique

    def update_test_result(self):
        TestUnique.objects.filter(
            ids=self.test_unique.id
        ).update(
            test_result=self.test_result
        )

    def update_components(self):
        self.set_component_stats()
        self.set_all_components()

        # sorulardaki soru parçalarını birleştirelim ve tekleştirelim.
        for component in self.__all_components:
            self.update_component_status(component)

    def update_questions(self):

        test_questions = self.__test.object.questions.all()

        self.__total = len(test_questions)

        for test_question in test_questions:

            question = QuestionRepository(question=test_question)

            question.request = self.__request
            question.test_unique = self.__test_unique

            question.set_components()
            question.set_code()
            question.set_true_answer()
            question.create_stat()

            i = 0
            # post edilen soru cevaplarına göre veri tabanında gerekli düzenlemeleri yapalım
            for answer in self.answers:

                question_answer = QuestionAnswer.objects.get(pk=answer['answer_id'])
                question.create_answer(question_answer=question_answer)

                # Eğer post edilen cevaplar içerisinde bu soru için cevap bulunduysa
                if answer['question_id'] == test_question.id:
                    i = i + 1

                    # Eğer post edilen cevap doğru ise
                    if question.answer.answer_is_true():
                        if question.components:
                            self.__true_components.append(question.stat.add_true())

                        self.__true = self.__true + 1

                    # Eğer post edilen cevap yanlış ise
                    else:
                        if question.components:
                            component_answers = ComponentAnswer.objects.select_related(
                                'component'
                            ).filter(question_answer_id=question_answer.id).all()

                            if len(component_answers) > 0:
                                # sorudaki soru parçaları için gerekli işlemleri yapalım

                                for component_answer in component_answers:

                                    c = ComponentRepository(component=component_answer.component)
                                    c.create_stat()
                                    c.stat.question = question
                                    c.stat.request = self.__request
                                    c.stat.test_unique = self.__test_unique

                                    if component_answer.component_ok == 1:
                                        # soru parçasını doğru soru parçası listesine ekleyelim
                                        self.__true_components.append(c.stat.add_true())
                                    else:
                                        # soru parçasını yanlış soru parçası listesine ekleyelim
                                        self.__false_components.append(c.stat.add_false())
                            else:
                                # soru parçasını yanlış soru parçası listesine ekleyelim
                                self.__false_components.append(question.stat.add_false())

                        self.__false = self.__false + 1

            # Eğer post edilen cevaplar içerisinde bu soru için cevap bulunamadıysa
            if i == 0:
                if question.components:
                    # soru parçasını boş soru parçası listesine ekleyelim
                    self.__empty_components.append(question.stat.add_empty())

                # boş soru sayısını bir artıralım
                self.__empty = self.__empty + 1

            if question.components:
                # question unique oluşturularım ve istatistikleri ekleyelim
                question.create_unique()
                question.unique.answer_is_true = question.answer.answer_is_true
                question.unique.update_stats()

