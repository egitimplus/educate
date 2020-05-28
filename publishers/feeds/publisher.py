from library.mixins import RequestMixin


class PublisherRepository(RequestMixin):

    def __init__(self, **kwargs):
        self._queryset = kwargs.pop("publisher", None)

    def publisher_group_manager_id(self):
        group = self._queryset.group

        if not group:
            return 0
        return group.user_id

    def publisher_manager_ids(self):
        return self._queryset.manager.all().values_list('id', flat=True)


