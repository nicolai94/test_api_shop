from carts.models import Cart, CartItem
from carts.serializers.nested.cart import ShortCartItemSerializer, ShortCreateCartItemSerializer, \
    ShortUpdateCartItemSerializer
from common.serializers.mixins import ExtendedModelSerializer


class CartItemSerializer(ExtendedModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(ExtendedModelSerializer):
    cart_item = ShortCartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            "id",
            "user",
            "ordered",
            "total_price",
            "cart_item",
        )


class CreateCartSerializer(ExtendedModelSerializer):
    cart_item = ShortCreateCartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            "user",
            "ordered",
            "cart_item",
        )


class UpdateCartSerializer(ExtendedModelSerializer):
    cart_item = ShortUpdateCartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            "user",
            "ordered",
            "cart_item",
        )