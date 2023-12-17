from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView
from products.urls import urlpatterns as products_urls
from orders.urls import urlpatterns as orders_urls
from carts.urls import urlpatterns as carts_urls

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("api.urls")),
    path("schema", SpectacularAPIView.as_view(), name="schema"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)

urlpatterns += products_urls
urlpatterns += orders_urls
urlpatterns += carts_urls
