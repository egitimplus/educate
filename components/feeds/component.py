from components.models import ComponentAnswerStat, ComponentStat
from library.feeds import search_id
from components.feeds import ComponentStatRepository
from library.mixins import TestUniqueMixin, RequestMixin


class ComponentRepository(TestUniqueMixin, RequestMixin):
    _stat = None
    _data = {
        'sub_components': [],
        'all_sub_components': [],
        'parent_components': [],
        'all_parent_components': [],
        'data_components': [],
    }
    _counts = False
    _status = False

    def __init__(self, **kwargs):
        self._object = kwargs.pop("component", None)

    # soru parçası bilgileri
    def detail(self):
        data = {
            'id': self._object.id,
            'name': self._object.name,
            'level': self._object.level
        }

        if self._counts:
            data['counts'] = self.component_count()

        if self._status:
            data['status'] = self.component_status()

        return data

    # soru parçasına ait 1. dereceden alt soru parçaları
    def sub_components(self):
        for item in self._object.source_component.all():
            self._object = item
            if search_id(item.id, self._data['sub_components']):
                continue
            else:
                child = self.detail()
                self._data['sub_components'].append(child)

    # soru parçasının bulunduğu 1. dereceden üst soru parçaları
    def parent_components(self):
        for item in self._object.to_component.all():
            self._object = item
            if search_id(item.id, self._data['parent_components']):
                continue
            else:
                child = self.detail()
                self._data['parent_components'].append(child)

    # soru parçasına ait tüm alt soru parçaları
    def all_sub_components(self):
        for item in self._object.source_component.all():
            self._object = item
            if search_id(item.id, self._data['all_sub_components']):
                continue
            else:
                child = self.detail()
                self._data['all_sub_components'].append(child)
                self.all_sub_components()

    # soru parçasının bulunduğu tüm üst soru parçaları
    def all_parent_components(self):
        for item in self._object.to_component.all():
            self._object = item
            if search_id(item.id, self._data['all_parent_components']):
                continue
            else:
                child = self.detail()
                self._data['all_parent_components'].append(child)
                self.all_parent_components()

    def data_component(self):
        self.sub_components()
        self.all_sub_components()

        data = {
            'id': self._object.id,
            'name': self._object.name,
            'level': self._object.level,
            'sub_components': self.component_format(self._data['sub_components'], 'list'),
            'all_sub_components': self.component_format(self._data['all_sub_components'], 'list')
        }

        return data

    def data_components(self):
        for component in self._object.source_component.all():
            self._object = component
            if search_id(component.id, self._data['data_components']):
                continue
            else:

                child = self.data_component()
                self._data['data_components'].append(child)
                self.data_components()

    # kullanıcı tarafından o soru parçası için cevaplanan adet
    # TODO Counts calısıyormu kontrol edilmeli
    def component_count(self):
        return ComponentAnswerStat.objects.filter(
            component=self._object,
            user=self._request.user
        ).count()

    # kullanıcının o soru parçası için durumu
    # TODO Status calısıyormu kontrol edilmeli
    def component_status(self):
        component = ComponentStat.objects.filter(
            component=self._object,
            user=self._request.user
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
                    self._data['all_components'] = self._data['all_sub_components'] + self._data['parent_components']

                data[key] = self.component_format(self._data[key], value)

        return data

    @property
    def stat(self):
        return self._stat

    def create_stat(self):
        self._stat = ComponentStatRepository(component=self)

    @property
    def object(self):
        return self._object
