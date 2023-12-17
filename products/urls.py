from django.urls import path

from products.views.products import product_detail, all_products

urlpatterns = [
    path("api/products", all_products, name="products"),
    path("api/product/<int:pk>", product_detail, name="product"),
    # path("api/categories", all_categories, name="categories"),
    # path("api/category/<int:pk>", category_detail, name="category"),
    # path("api/product/filters", get_filters, name="product_filters"),
    # path("api/product/rating", product_rating, name="update_rating"),
]
