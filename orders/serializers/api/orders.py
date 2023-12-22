from common.serializers.mixins import ExtendedModelSerializer
from orders.models import Order
from orders.models.orders import OrderProduct


class OrderProductSerializer(ExtendedModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'quantity')


class OrderSerializer(ExtendedModelSerializer):
    products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'products', 'created_at')