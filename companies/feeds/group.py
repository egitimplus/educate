from library.mixins import RequestMixin


class GroupRepository(RequestMixin):

    def __init__(self, **kwargs):
        self._queryset = kwargs.pop("group", None)







