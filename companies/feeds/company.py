from library.mixins import RequestMixin


class CompanyRepository(RequestMixin):

    @property
    def managers(self):
        return self._object.manager.all()

    @property
    def group_manager(self):
        return self._object.group.user
