from library.feeds import DynamicModelSerializer
from universities.models import Discount


class DiscountSerializer(DynamicModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'name')