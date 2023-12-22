from django.urls import path

from orders.views.orders import create_order

urlpatterns = [
    path("api/order", create_order, name="order"),
]
