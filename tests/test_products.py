# import pytest
#
# from products.models import Product, Category
#
#
# @pytest.mark.django_db
# def test_get_products(client):
#     category = Category(
#         name="test_category",
#         slug="test_slug",
#     )
#     category.save()
#     product1 = Product(
#         name="test",
#         price=120,
#         slug="test",
#         description="test description",
#         quantity=12,
#         category=category,
#     )
#     product1.save()
#     product2 = Product(
#         name="test22",
#         price=120,
#         slug="test2",
#         description="test description",
#         quantity=12,
#         category=category,
#     )
#     product2.save()
#
#     response = client.get(f"/api/products", follow=True)
#     assert response.status_code == 200
#     assert len(response.data) == 2
#
#
# @pytest.mark.django_db
# def test_get_product(client):
#     category = Category(
#         name="test_category",
#         slug="test_slug",
#     )
#     category.save()
#     product1 = Product(
#         name="test",
#         price=120,
#         slug="test",
#         description="test description",
#         quantity=12,
#         category=category,
#     )
#     product1.save()
#
#     response = client.get(f"/api/products/{product1.id}", follow=True)
#
#     assert response.status_code == 200
#     assert response.data["name"] == product1.name
#     assert response.data["price"] == product1.price
#     assert response.data["description"] == product1.description
