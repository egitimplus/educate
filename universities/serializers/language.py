from library.feeds import DynamicModelSerializer
from universities.models import Language


class LanguageSerializer(DynamicModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'short_name')
