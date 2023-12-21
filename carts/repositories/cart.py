from django.contrib.auth.models import User

from carts.models import Cart


class CartRepository:
    def get_cart_by_user(self, user: User):
        return Cart.objects.prefetch_related('cart_item').filter(user=user)
