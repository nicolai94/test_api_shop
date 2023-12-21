from common.serializers.mixins import ExtendedModelSerializer
from orders.models import Order


class OrderSerializer(ExtendedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
