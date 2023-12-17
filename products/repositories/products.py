from products.models import Product


class ProductRepository:
    def get_all_products(self):
        return Product.objects.all()

    def get_product_by_id(self, product_id: int):
        return Product.objects.get(pk=product_id)
