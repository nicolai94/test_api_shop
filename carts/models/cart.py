from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

from products.exceptions import ProductDoesNotExistException
from products.models import Product
from django.db.models.signals import post_save


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return f'Cart for {self.user.username}'

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
        ordering = ("-id", )


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_item')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'Cart Item for {self.user.username} and cart {self.cart.pk}'

    class Meta:
        verbose_name = "Товар корзины"
        verbose_name_plural = "Товары корзины"
        ordering = ("-id", )


@receiver(post_save, sender=CartItem)
def correct_price(sender, **kwargs):
    cart_item = kwargs["instance"]

    try:
        product = Product.objects.get(id=cart_item.product.pk)
    except Product.DoesNotExist:
        raise ProductDoesNotExistException

    cart_item.price = cart_item.quantity * float(product.price)
