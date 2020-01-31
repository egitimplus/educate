from library.feeds import DynamicModelSerializer
from universities.models import Property


class ConditionSerializer(DynamicModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'department', 'name', 'value', 'created', 'updated')