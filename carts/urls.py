from django.urls import path

from carts.views.cart import get_cart, create_cart, update_cart, delete_cart

urlpatterns = [
    path("api/cart", get_cart, name="cart"),
    path("api/cart/create", create_cart, name="create_cart"),
    path("api/cart/update", update_cart, name="update_cart"),
    path("api/cart/delete", delete_cart, name="delete_cart"),
]
