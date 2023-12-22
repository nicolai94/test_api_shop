import logging

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response

from backends import CustomTokenAuthentication
from carts.exceptions import CartDoesNotExistException
from carts.models import Cart
from orders.models import Order
from orders.serializers.api.orders import OrderSerializer

logger = logging.getLogger("main")


@extend_schema(summary="Создать заказ", tags=["Заказ"])
@api_view(['POST'])
@authentication_classes([CustomTokenAuthentication])
def create_order(request: Request):
    user = request.user
    carts = Cart.objects.filter(user=user)

    if not carts:
        logger.info("Cart not found")
        raise CartDoesNotExistException

    order = Order.objects.create(user=user)

    for cart in carts:
        cart_items = cart.cart_item.all()
        for item in cart_items:
            order.products.add(item.product)
    order.save()
    carts.delete()

    serializer = OrderSerializer(order)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
