from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from products.models import Category
from products.serializers.api.category import CategorySerializer


@extend_schema(
    summary="Список категорий",
    tags=["Категории"],
    responses=CategorySerializer,
)
@api_view(['GET'])
def get_category_tree(request: Request):
    categories = Category.objects.filter(parent__isnull=True)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
