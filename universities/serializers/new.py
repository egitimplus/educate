from library.feeds import DynamicModelSerializer
from universities.models import New


class NewSerializer(DynamicModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'university', 'title', 'image', 'slug', 'body', 'created', 'updated')