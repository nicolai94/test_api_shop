from django.urls import path, include
from rest_framework import routers

from carts.views.carts import CartViewSet, CartItemViewSet

# from carts.views.carts import cart_detail

router = routers.DefaultRouter()

router.register("carts", CartViewSet)
router.register("cart_items", CartItemViewSet)


urlpatterns = [
    path("", include(router.urls)),
    # path("api/cart", cart_detail, name="cart"),
]
