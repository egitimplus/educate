from library.mixins import RequestMixin


class GroupRepository(RequestMixin):

    def __init__(self, **kwargs):
        self._object = kwargs.pop("group", None)







