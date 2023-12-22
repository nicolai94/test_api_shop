from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView

from common.views.auth import user_logout, user_login
from products.urls import urlpatterns as products_urls
from orders.urls import urlpatterns as orders_urls
from carts.urls import urlpatterns as carts_urls

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("api.urls")),
    path("schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/auth/login", user_login, name="user_login"),
    path("api/auth/logout", user_logout, name="user_log"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)

urlpatterns += products_urls
urlpatterns += orders_urls
urlpatterns += carts_urls
urlpatterns += orders_urls
