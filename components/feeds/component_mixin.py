from components.feeds import ComponentRepository
from library.feeds import search_id


class ComponentMixin:
    # soruya ait 1. dereceden alt soru tiplerini alt elemanları ile döndürür
    def data_sub_components(self):
        data = []

        for component in self.__object.component.all():
            cr = ComponentRepository(component=component)
            cr.request = self.__request
            cr.sub_components()

            data = cr.component_formats(
                sub_components='list'
            )

            data.append(data['sub_components'])

        return data

    # soruya ait tüm alt soru tiplerini alt elemanları ile döndürür
    def data_all_sub_components(self):
        data = []

        for component in self.__object.component.all():
            cr = ComponentRepository(component=component)
            cr.request = self.__request
            sub = cr.data_component()
            cr.data_components()

            data = cr.component_formats(
                data_components='list'
            )

            if not search_id(component.id, data):
                data.append(sub)

            for sub_component in data['data_components']:
                if not search_id(sub_component['id'], data):
                    data.append(sub_component)

        return data

    def all_components(self, **kwargs):

        return_format = kwargs.pop("return_format", 'dict')
        counts = kwargs.pop("counts", None)
        status = kwargs.pop("status", None)

        all_components = []

        for component in self.__object.component.all():

            cr = ComponentRepository(component=component)
            cr.request = self.__request
            cr.counts = counts
            cr.status = status
            cr.all_sub_components()

            parent_component = cr.component()

            if return_format == 'dict':
                if not search_id(component.id, all_components):
                    all_components.append(parent_component)
            else:
                if component.id not in all_components:
                    all_components.append(parent_component['id'])

            data = cr.component_formats(
                all_sub_components=return_format
            )

            for sub_component in data['all_sub_components']:

                if return_format == 'dict':
                    if not search_id(sub_component['id'], all_components):
                        all_components.append(sub_component)
                else:
                    if sub_component not in all_components:
                        all_components.append(sub_component)

        return all_components

    def sub_components(self, **kwargs):

        return_format = kwargs.pop("return_format", 'dict')
        counts = kwargs.pop("counts", None)
        status = kwargs.pop("status", None)

        data = []

        for component in self.__object.component.all():
            cr = ComponentRepository(component=component)
            cr.request = self.__request
            cr.counts = counts
            cr.status = status
            child = cr.component()
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

        for component in self.__object.component.all():
            cr = ComponentRepository(component=component)
            cr.request = self.__request
            cr.counts = counts
            cr.status = status
            item = cr.component()
            cr.all_sub_components()

            if return_format == 'dict':
                if not search_id(component.id, data):
                    data.append(item)
            else:
                if component.id not in data:
                    data.append(item['id'])

            data = cr.component_formats(
                all_sub_components=return_format
            )

            for sub_item in data['all_sub_components']:
                if return_format == 'dict':
                    if not search_id(sub_item['id'], data):
                        data.append(sub_item)
                else:
                    if sub_item not in data:
                        data.append(sub_item)

        return data
