from rest_framework import serializers

from carts.models.carts import Cart, CartItem
from common.serializers.mixins import ExtendedModelSerializer
from products.serializers.api.products import SimpleProductSerializer


class CartItemSerializer(ExtendedModelSerializer):
    product = SimpleProductSerializer()
    sub_total = serializers.SerializerMethodField(method_name="total")

    class Meta:
        model = CartItem
        fields = ('id', "cart", "product", "quantity", "sub_total")

    def total(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.price


class CartSerializer(ExtendedModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField(method_name="main_total")

    class Meta:
        model = Cart
        fields = ('id', "items", "grand_total")

    def main_total(self, cart: Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])

        return total


class AddCartItemSerializer(ExtendedModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ('id', "product_id", "quantity")

