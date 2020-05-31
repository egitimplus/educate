from library.mixins import RequestMixin


class CompanyRepository(RequestMixin):

    @property
    def managers(self):
        return self.__object.manager.all()

    @property
    def group_manager(self):
        return self.__object.group.user
