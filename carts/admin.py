from django.contrib import admin

from carts.models.carts import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    fields = ("product", "quantity")
    extra = 1


@admin.register(CartItem)
class CartItem(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at"]
    inlines = [CartItemInline]
