from django.urls import path

from products.views.category import get_category_tree
from products.views.products import product_detail, all_products

urlpatterns = [
    path("api/products", all_products, name="products"),
    path("api/product/<int:pk>", product_detail, name="product"),
    path("api/categories", get_category_tree, name="categories"),
]
