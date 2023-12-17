from carts.models.carts import Cart


class CartRepository:

    def get_product_by_id(self, product_id: int):
        return Cart.objects.get(pk=product_id)
