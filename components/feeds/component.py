from components.models import ComponentAnswerStat, ComponentStat
from library.feeds import search_id
from questions.models import QuestionAnswerStat


class ComponentRepository:

    def __init__(self, request, **kwargs):
        self.counts = kwargs.pop("counts", None)
        self.status = kwargs.pop("status", None)
        self.request = request

    def component(self, component):
        data = {
            'id': component.id,
            'name': component.name,
            'level': component.level
        }
        if self.counts:
            data['counts'] = self.component_count(component.id)

        if self.status:
            data['status'] = self.component_status(component.id)

        return data

    def sub_components(self, queryset, **kwargs):

        return_format = kwargs.pop("return_format", 'dict')
        data = []
        for component in queryset.source_component.all():

            child = self.component(component)
            data.append(child)

        return self.component_format(data, return_format=return_format)

    def parent_components(self, queryset, **kwargs):

        return_format = kwargs.pop("return_format", 'dict')

        data = []
        for component in queryset.to_component.all():
            child = self.component(component)
            data.append(child)

        return self.component_format(data, return_format=return_format)

    def all_sub_components(self, queryset, data=[], **kwargs):

        return_format = kwargs.pop("return_format", 'dict')

        for component in queryset.source_component.all():
            c = search_id(component.id, data)
            if c:
                continue
            else:
                child = self.component(component)
                data.append(child)
                self.all_sub_components(component, data)

        return self.component_format(data, return_format=return_format)

    def all_parent_components(self, queryset, data=[], **kwargs):

        return_format = kwargs.pop("return_format", 'dict')

        for component in queryset.to_component.all():
            c = search_id(component.id, data)
            if c:
                continue
            else:
                child = self.component(component)
                data.append(child)

                self.all_parent_components(component, data)

        return self.component_format(data, return_format=return_format)

    def all_component_types(self, queryset, **kwargs):

        sub_components = kwargs.pop("sub_components", None)
        data_components = kwargs.pop("data_components", None)
        all_sub_components = kwargs.pop("all_sub_components", None)
        parent_components = kwargs.pop("parent_components", None)
        all_components = kwargs.pop("all_components", None)

        r = dict()

        if sub_components or all_sub_components:
            data = []
            sub = []
            i = 0
            for component in queryset.source_component.all():

                i = i + 1
                c = search_id(component.id, data)
                if c:
                    continue
                else:
                    child = self.component(component)
                    data.append(child)

                    ''' if i == 1: '''
                    if sub_components:
                        sub.append(child)

                    if all_sub_components:
                        self.all_sub_components(component, data)

        if all_sub_components:
            r['all_sub_components'] = self.component_format(data, return_format=all_sub_components)

        if sub_components:
            r['sub_components'] = self.component_format(sub, return_format=sub_components)

        if parent_components:
            r['parent_components'] = self.parent_components(queryset, return_format=parent_components)

        if all_components:
            r['all_components'] = r['all_sub_components'] + r['parent_components']

        if data_components:
            r['data_components'] = self.component_format(sub, return_format=data_components)

        return r

    def data_component(self, queryset, **kwargs):

        return_format = kwargs.pop("return_format", 'list')

        sub = self.sub_components(queryset=queryset, data=[], return_format=return_format)
        all_sub = self.all_sub_components(queryset=queryset, data=[], return_format=return_format)

        data = {
            'id': queryset.id,
            'name': queryset.name,
            'level': queryset.level,
            'sub_components': sub,
            'all_sub_components': all_sub
        }

        return data

    def data_components(self, queryset, data=[], **kwargs):

        return_format = kwargs.pop("return_format", 'list')

        for component in queryset.source_component.all():

            c = search_id(component.id, data)
            if c:
                continue
            else:

                child = self.data_component(queryset=component, data=[], return_format=return_format)
                data.append(child)

                self.data_components(component, data, return_format=return_format)

        return data

    def component_format(self, components, **kwargs):

        return_format = kwargs.pop("return_format", 'dict')

        if return_format == 'dict':
            return components
        else:
            all_components = list()
            for component in components:
                    all_components.append(component['id'])

        return all_components

    # TODO Counts calısıyormu kontrol edilmeli
    def component_count(self, component_id):
        return ComponentAnswerStat.objects.filter(component_id=component_id, user_id=self.request.user.id).count()

    # TODO Status calısıyormu kontrol edilmeli
    def component_status(self, component_id):
        component = ComponentStat.objects.filter(component_id=component_id, user_id=self.request.user.id).first()
        if not component:
            return 0
        return component.component_status


class ComponentPartRepository:

    def __init__(self, request, source):
        self.source = source
        self.request = request

    def data_sub_components(self):
        """
        soruya ait 1. dereceden alt soru tiplerini alt elemanları ile döndürür
        """
        data = []
        component_repo = ComponentRepository(request=self.request)

        for component in self.source.component.all():
            sub = component_repo.data_component(queryset=component, data=[], return_format='list')
            data.append(sub)

        return data

    def data_all_sub_components(self):
        """
        soruya ait tüm alt soru tiplerini alt elemanları ile döndürür
        """
        data = []
        component_repo = ComponentRepository(request=self.request)

        for component in self.source.component.all():
            sub = component_repo.data_component(queryset=component, data=[], return_format='list')
            sub_child = component_repo.data_components(queryset=component, data=[], return_format='list')

            if not search_id(match=component.id, data=data):
                data.append(sub)

            for sub_component in sub_child:
                if not search_id(match=sub_component['id'], data=data):
                    data.append(sub_component)

        return data

    def all_components(self, **kwargs):

        return_format = kwargs.pop("return_format", 'dict')
        counts = kwargs.pop("counts", None)
        status = kwargs.pop("status", None)

        all_components = []

        component_repo = ComponentRepository(request=self.request, counts=counts, status=status)

        for component in self.source.component.all():
            parent_component = component_repo.component(component)

            if return_format == 'dict':
                if not search_id(match=component.id, data=all_components):
                    all_components.append(parent_component)
            else:
                if component.id not in all_components:
                    all_components.append(parent_component['id'])

            sub_components = component_repo.all_sub_components(component, data=[])
            for sub_component in sub_components:

                if return_format == 'dict':
                    if not search_id(match=sub_component['id'], data=all_components):
                        all_components.append(sub_component)
                else:
                    if sub_component['id'] not in all_components:
                        all_components.append(sub_component['id'])

        return all_components

    def sub_components(self, **kwargs):

        return_format = kwargs.pop("return_format", 'dict')
        counts = kwargs.pop("counts", None)
        status = kwargs.pop("status", None)

        data = []

        component_repo = ComponentRepository(request=self.request, counts=counts, status=status)

        for component in self.source.component.all():

            child = component_repo.component(component)
            if return_format == 'dict':
                data.append(child)
            else:
                data.append(child['id'])

        return data

    def all_sub_components(self, **kwargs):

        return_format = kwargs.pop("return_format", 'dict')
        counts = kwargs.pop("counts", None)
        status = kwargs.pop("status", None)

        data = []

        component_repo = ComponentRepository(request=self.request, counts=counts, status=status)

        for component in self.source.component.all():
            item = component_repo.component(component)

            if return_format == 'dict':
                if not search_id(match=component.id, data=data):
                    data.append(item)
            else:
                if component.id not in data:
                    data.append(item['id'])

            sub_items = component_repo.all_sub_components(component, data=[])
            for sub_item in sub_items:
                if return_format == 'dict':
                    if not search_id(match=sub_item['id'], data=data):
                        data.append(sub_item)
                else:
                    if sub_item['id'] not in data:
                        data.append(sub_item['id'])

        return data

    def have_answer_stat(self):
        """
        kullanıcılar soruyu daha önce çözmüş mü ?
        """
        have_answer = QuestionAnswerStat.objects.filter(question_id=self.source.id).exists()
        if have_answer:
            return True

        return False


class ComponentIdRepository:

    def __init__(self, request):
        self.request = request

    def sub_components(self, queryset):

        data = []
        for component in queryset.source_component.all():
            data.append(component.id)

        return data

    def all_sub_components(self, queryset, data=[]):

        for component in queryset.source_component.all():
            data.append(component.id)
            self.all_sub_components(component, data)

        return data
