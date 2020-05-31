from library.mixins import RequestMixin


class CategoryRepository(RequestMixin):

    def __init__(self, **kwargs):
        self.__object = kwargs.pop("category", None)








