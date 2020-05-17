from components.models import ComponentAnswerStat, ComponentStat
from library.feeds import search_id


class ComponentRepository:

    def __init__(self, request, **kwargs):
        self.request = request
        self.component = kwargs.pop("component", None)
        self.counts = kwargs.pop("counts", None)
        self.status = kwargs.pop("status", None)
        self.data = {
            'sub_components': [],
            'all_sub_components': [],
            'parent_components': [],
            'all_parent_components': [],
            'data_components': [],
        }

    # soru parçası bilgileri
    def detail(self):
        data = {
            'id': self.component.id,
            'name': self.component.name,
            'level': self.component.level
        }

        if self.counts:
            data['counts'] = self.component_count()

        if self.status:
            data['status'] = self.component_status()

        return data

    # soru parçasına ait 1. dereceden alt soru parçaları
    def sub_components(self):
        for item in self.component.source_component.all():
            self.component = item
            if search_id(item.id, self.data['sub_components']):
                continue
            else:
                child = self.detail()
                self.data['sub_components'].append(child)

    # soru parçasının bulunduğu 1. dereceden üst soru parçaları
    def parent_components(self):
        for item in self.component.to_component.all():
            self.component = item
            if search_id(item.id, self.data['parent_components']):
                continue
            else:
                child = self.detail()
                self.data['parent_components'].append(child)

    # soru parçasına ait tüm alt soru parçaları
    def all_sub_components(self):
        for item in self.component.source_component.all():
            self.component = item
            if search_id(item.id, self.data['all_sub_components']):
                continue
            else:
                child = self.detail()
                self.data['all_sub_components'].append(child)
                self.all_sub_components()

    # soru parçasının bulunduğu tüm üst soru parçaları
    def all_parent_components(self):
        for item in self.component.to_component.all():
            self.component = item
            if search_id(item.id, self.data['all_parent_components']):
                continue
            else:
                child = self.detail()
                self.data['all_parent_components'].append(child)
                self.all_parent_components()

    def data_component(self):

        self.sub_components()
        self.all_sub_components()

        data = {
            'id': self.component.id,
            'name': self.component.name,
            'level': self.component.level,
            'sub_components': self.component_format(self.data['sub_components'], 'list'),
            'all_sub_components': self.component_format(self.data['all_sub_components'], 'list')
        }

        return data

    def data_components(self):

        for component in self.component.source_component.all():
            self.component = component
            if search_id(component.id, self.data['data_components']):
                continue
            else:

                child = self.data_component()
                self.data['data_components'].append(child)
                self.data_components()

    # kullanıcı tarafından o soru parçası için cevaplanan adet
    # TODO Counts calısıyormu kontrol edilmeli
    def component_count(self):
        return ComponentAnswerStat.objects.filter(
            component=self.component,
            user=self.request.user
        ).count()

    # kullanıcının o soru parçası için durumu
    # TODO Status calısıyormu kontrol edilmeli
    def component_status(self):
        component = ComponentStat.objects.filter(
            component=self.component,
            user=self.request.user
        ).first()

        if not component:
            return 0
        return component.component_status

    # döndürülecek olan format tipi
    def component_format(self, data, return_format):
        if return_format == 'dict':
            return data
        else:
            return_data = list()
            for component in data:
                return_data.append(component['id'])

            return return_data

    def component_formats(self, **kwargs):
        data = dict()

        for key, value in kwargs.items():
            if value is not None:
                if key == 'all_components':
                    self.data['all_components'] = self.data['all_sub_components'] + self.data['parent_components']

                data[key] = self.component_format(self.data[key], value)

        return data

