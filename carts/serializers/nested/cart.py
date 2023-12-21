from carts.models import CartItem
from common.serializers.mixins import ExtendedModelSerializer


class ShortCartItemSerializer(ExtendedModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            "id",
            "quantity",
            "product",
        )


class ShortCreateCartItemSerializer(ExtendedModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            "quantity",
        )


class ShortUpdateCartItemSerializer(ExtendedModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            "id",
            "quantity",
            "product",

        )
