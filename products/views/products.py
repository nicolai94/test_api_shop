import logging

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from products.exceptions import ProductDoesNotExistException
from products.models import Product, Category
from products.repositories.products import ProductRepository
from products.serializers.api.products import ProductRetrieveSerializer, ProductListSerializer
from products.services.products import resolve_query_params

logger = logging.getLogger("main")


@extend_schema(summary="Деталка товара", tags=["Товары"], responses=ProductRetrieveSerializer)
@api_view(["GET"])
def product_detail(request: Request, pk: int) -> Response:
    try:
        product_repo = ProductRepository()
        product = product_repo.get_product_by_id(pk)
    except Product.DoesNotExist as e:
        logger.info(f"Product not found: {e}")
        raise ProductDoesNotExistException

    serializer = ProductRetrieveSerializer(product)

    return Response(serializer.data)


@extend_schema(
    summary="Список товаров",
    tags=["Товары"],
    responses=ProductListSerializer,
    parameters=[
        OpenApiParameter(name="price_min", type=int, description="Активен", required=False),
        OpenApiParameter(name="price_max", type=int, description="Активен", required=False),
        OpenApiParameter(
            name="category",
            type=str,
            description="Категория",
            required=False,
            enum=[cat.name for cat in Category.objects.all()],
        ),
    ],
)
@api_view(["POST"])
def all_products(request: Request) -> Response:
    price_min = request.GET.get("price_min")
    price_max = request.GET.get("price_max")
    category = request.GET.get("category")

    product_repo = ProductRepository()
    queryset = product_repo.get_all_products()
    filtered_queryset = resolve_query_params(queryset, price_min, price_max, category)

    if not filtered_queryset:
        logger.info("Product not found")
        raise ProductDoesNotExistException

    serializer = ProductListSerializer(instance={"total_count": len(filtered_queryset), "products": filtered_queryset})

    return Response(serializer.data)
