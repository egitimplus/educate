from library.feeds import DynamicModelSerializer
from universities.models import Department


class DepartmentSerializer(DynamicModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'section', 'language', 'discount', 'tag', 'faculty', 'title', 'slug', 'content',
                  'education_type', 'base_point', 'ranking', 'is_undergraduate', 'created', 'updated')


