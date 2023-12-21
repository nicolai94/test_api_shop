import pytest

from products.models import Product


@pytest.fixture
def product():
    def product():
        product = Product(
            name="test",
            quantity=12,
        )
        product.save()

    return product
