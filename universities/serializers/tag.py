from library.feeds import DynamicModelSerializer
from universities.models import Tag


class TagSerializer(DynamicModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')