from django.contrib import admin
from django.utils.safestring import mark_safe
from products.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ("image",)
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "quantity", "created_at", "updated_at", "get_image"]
    list_filter = ["created_at", "updated_at"]
    list_editable = ["price"]
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline]

    def get_image(self, obj):
        if obj.images.first():
            return mark_safe(f'<image src={obj.images.first().image.url} width="100" height = "110"')

        return None

    get_image.short_description = "Image"
