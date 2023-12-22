import logging

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response

from backends import CustomTokenAuthentication
from carts.exceptions import CartDoesNotExistException, CartItemDoesNotExistException
from carts.models import Cart, CartItem
from carts.repositories.cart import CartRepository
from carts.serializers.api.cart import CartSerializer, CreateCartSerializer, UpdateCartSerializer, CartItemSerializer
from products.exceptions import ProductDoesNotExistException
from products.models import Product

logger = logging.getLogger("main")


@extend_schema(summary="Деталка корзины", tags=["Корзина"], responses=CartSerializer)
@api_view(["GET"])
@authentication_classes([CustomTokenAuthentication])
def get_cart(request: Request):
    user = request.user
    cart_repo = CartRepository()
    cart = cart_repo.get_cart_by_user(user)
    cart_items = CartItem.objects.filter(cart__in=cart)
    if not cart:
        logger.info(f"Cart not found")
        raise CartDoesNotExistException

    serializer = CartItemSerializer(cart_items, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(summary="Создание корзины", tags=["Корзина"], request=CreateCartSerializer)
@api_view(["POST"])
@authentication_classes([CustomTokenAuthentication])
def create_cart(request: Request):
    if request.method == "POST":
        data = request.data
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user, ordered=False)
        try:
            product = Product.objects.get(id=data.get('product'))
        except Product.DoesNotExist as e:
            logger.info(f"Product not found: {e}")
            raise ProductDoesNotExistException

        price = product.price
        quantity = data.get('quantity')
        cart_items = CartItem(user=user, product=product, cart=cart, price=price, quantity=quantity)
        cart_items.save()

        total_price = 0
        cart_items = CartItem.objects.filter(user=user, cart=cart.id)
        if not cart_items:
            logger.info(f"Cart Item not found")
            raise CartItemDoesNotExistException

        for item in cart_items:
            total_price += item.price
        cart.total_price = total_price
        cart.save()

        return Response({"Success": "Added cart"})


@extend_schema(summary="Изменить корзину", tags=["Корзина"], request=UpdateCartSerializer)
@api_view(["PUT"])
@authentication_classes([CustomTokenAuthentication])
def update_cart(request: Request):
    data = request.data
    try:
        cart_item = CartItem.objects.get(id=data.get('id'))
    except CartItem.DoesNotExist as e:
        logger.info(f"Cart Item not found: {e}")
        raise CartItemDoesNotExistException
    quantity = data.get('quantity')
    cart_item.quantity += quantity
    cart_item.save()

    return Response({"Success": "Items updated"})


@extend_schema(summary="Удалить корзину", tags=["Корзина"])
@api_view(["DELETE"])
@authentication_classes([CustomTokenAuthentication])
def delete_cart(request: Request):
    data = request.data
    user = request.user
    try:
        cart_item = CartItem.objects.get(id=data.get('id'))
    except CartItem.DoesNotExist as e:
        logger.info(f"Cart Item not found: {e}")
        raise CartItemDoesNotExistException

    cart_item.delete()

    cart = Cart.objects.filter(user=user, ordered=False).first()
    queryset = CartItem.objects.filter(cart=cart)
    serializer = CartItemSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
