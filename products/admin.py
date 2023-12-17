from django.contrib import admin
from django.utils.safestring import mark_safe
from django_mptt_admin.admin import DjangoMpttAdmin

from products.models import Product, ProductImage, Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ("image",)
    extra = 1


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    mptt_level_indent = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "quantity", "created_at", "updated_at", "get_image"]
    list_filter = ["created_at", "updated_at", "category"]
    list_editable = ["price"]
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ["category"]
    inlines = [ProductImageInline]

    def get_image(self, obj):
        if obj.images.first():
            return mark_safe(f'<image src={obj.images.first().image.url} width="100" height = "110"')

        return None

    get_image.short_description = "Image"
