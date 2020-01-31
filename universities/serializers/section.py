from library.feeds import DynamicModelSerializer
from universities.models import Section


class SectionSerializer(DynamicModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name')