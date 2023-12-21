from rest_framework import serializers

from products.models import Category


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        serializer = CategorySerializer(obj.get_children(), many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'parent', 'children')
