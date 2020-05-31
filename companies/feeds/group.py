from library.mixins import RequestMixin


class GroupRepository(RequestMixin):

    def __init__(self, **kwargs):
        self.__object = kwargs.pop("group", None)







