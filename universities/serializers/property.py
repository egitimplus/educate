from library.feeds import DynamicModelSerializer
from universities.models import Property


class PropertySerializer(DynamicModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'department','key', 'value', 'created', 'updated')
