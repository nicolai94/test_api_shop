from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from carts.models.carts import Cart, CartItem
from carts.repositories.carts import CartRepository
from carts.serializers.api.carts import CartSerializer, AddCartItemSerializer, CartItemSerializer
from products.exceptions import ProductDoesNotExistException
from products.models import Product


# @extend_schema(summary="Деталка корзины", tags=["Корзина"], responses=CartSerializer)
# @api_view(["GET"])
# def cart_detail(request: Request, pk: int) -> Response:
#     try:
#         product_repo = CartRepository()
#         product = product_repo.get_product_by_id(pk)
#     except Product.DoesNotExist:
#         raise ProductDoesNotExistException
#
#     serializer = CartSerializer(product)
#
#     return Response(serializer.data)


class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer

        return CartItemSerializer
