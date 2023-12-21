import pytest
from rest_framework.test import APIClient

from products.models import Product

pytest_plugins = [
    "tests.fixtures.product",
]


# @pytest.fixture
# def product():
#     def product():
#         p = Product(
#             name="test",
#             slug="test",
#             description="test description",
#             quantity=12,
#         )
#         p.save()
#
#     return product


@pytest.fixture
def client():
    return APIClient()


# @pytest.fixture
# def auth_client(user, client):
#     client.post("api/login", data={"email": user.email, "password": user.password})
#
#     return client


# @pytest.fixture(scope='session')
# def django_db_setup():
#     settings.DATABASES['default'] = {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
