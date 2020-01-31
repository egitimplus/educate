from library.feeds import DynamicModelSerializer
from universities.models import Faculty


class FacultySerializer(DynamicModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'province', 'university', 'title', 'slug', 'is_undergraduate', 'created', 'updated')
