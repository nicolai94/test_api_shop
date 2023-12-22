import pytest
from django.contrib.auth.models import User

from carts.models import Cart, CartItem
from products.models import Product


@pytest.fixture
def cart():
    user = User(username='test', password='test')
    user.save()
    cart = Cart(user=user)
    cart.save()
    product = Product(
        name='test_product',
        slug='test',
        description='test description',
        price=100,
        quantity=1,
    )
    product.save()
    cart_item = CartItem(cart=cart, user=cart.user, product=product)
    cart_item.save()

    return cart


@pytest.mark.django_db
def test_get_cart(client, cart):
    response = client.get("/api/cart")

    assert response.status_code == 200
