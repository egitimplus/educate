from library.feeds import DynamicModelSerializer
from universities.models import UniversityType


class UniversityTypeSerializer(DynamicModelSerializer):
    class Meta:
        model = UniversityType
        fields = ('id', 'name')