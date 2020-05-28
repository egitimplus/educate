from library.mixins import RequestMixin


class CategoryRepository(RequestMixin):

    def __init__(self, **kwargs):
        self._queryset = kwargs.pop("category", None)








