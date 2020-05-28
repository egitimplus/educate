from library.mixins import RequestMixin


class SchoolRepository(RequestMixin):

    def __init__(self, **kwargs):
        self._queryset = kwargs.pop("school", None)

    def manager_ids(self):
        return self._queryset.manager.all().values_list('id', flat=True)

    def group_manager_id(self):

        group = self._queryset.group

        if not group:
            return 0
        return group.user_id


