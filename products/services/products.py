from django.db.models import QuerySet

from products.models import Product


def resolve_query_params(
    queryset: QuerySet[Product],
    price_min: int,
    price_max: int,
    category: str,
) -> QuerySet[Product]:
    if price_min:
        queryset = queryset.filter(price__gte=price_min)
    if price_max:
        queryset = queryset.filter(price__lte=price_max)
    if category:
        queryset = queryset.filter(category__slug=category)

    return queryset
