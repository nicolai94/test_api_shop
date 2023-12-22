import pytest

from products.models import Category


@pytest.mark.django_db
def test_categories_tree(client):
    category = Category(
        name="test",
        slug='testt'
    )
    category.save()

    response = client.get("/api/categories")

    categories = Category.objects.all()

    assert response.status_code == 200
    assert len(categories) == 1
