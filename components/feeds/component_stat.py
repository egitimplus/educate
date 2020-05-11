from components.models import ComponentAnswerStat, ComponentStat
from library.feeds import search_id


class ComponentStatRepository:

    def __init__(self, request, **kwargs):
        self.stats = kwargs.pop("component_stats", None)
        self.components = kwargs.pop("components", None)
        self.request = request

    def update_component_status(self, component_id):

        true_component_diff = 10
        false_component_diff = 20
        true_component_percent = 50

        component_status = search_id(component_id, self.stats)

        data = {
            'status': 0,
            'percent': 0,
            'repeat': 0,
            'solved': component_status.solved + 1
        }

        if component_status:
            data['status'] = component_status.status
            data['percent'] = component_status.percent
            data['repeat'] = component_status.repeat

        true_count = self.components['true'].count(component_id)
        false_count = self.components['false'].count(component_id)
        # empty_count = self.components['empty'].count(component_id)

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
