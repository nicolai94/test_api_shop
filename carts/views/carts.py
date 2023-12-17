from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from carts.models.carts import Cart, CartItem
from carts.serializers.api.carts import CartSerializer, AddCartItemSerializer, CartItemSerializer


class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer

        return CartItemSerializer
