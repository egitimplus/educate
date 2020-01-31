from library.feeds import DynamicModelSerializer
from universities.models import University


class UniversitySerializer(DynamicModelSerializer):
    class Meta:
        model = University
        fields = ('id', 'type', 'province', 'name', 'image', 'content', 'contact_content', 'slug', 'created', 'updated')
