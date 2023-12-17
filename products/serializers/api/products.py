from rest_framework import serializers

from products.models import Product, ProductImage

from common.serializers.mixins import ExtendedModelSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image",)


class ProductRetrieveSerializer(ExtendedModelSerializer):
    # category = CategoryRetrieveSerializer()
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "created_at",
            "updated_at",
            "name",
            "slug",
            "description",
            "price",
            "quantity",
            "images",
        )


class ProductListSerializer(serializers.Serializer):
    total_count = serializers.IntegerField()
    products = ProductRetrieveSerializer(many=True)

    class Meta:
        fields = ("total_count", "products")


class SimpleProductSerializer(ExtendedModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price")
