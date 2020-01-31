from publishers.models import Publisher
from companies.models import CompanyGroup


class PublisherRepository:

    def __init__(self, request, **kwargs):
        self.request = request

    def publisher_group_manager_id(self, group_id):
        group = CompanyGroup.objects.filter(id=group_id).first()
        if not group:
            return 0
        return group.user_id

    def publisher_manager_ids(self, publisher):
        return publisher.manager.all().values_list('id', flat=True)


