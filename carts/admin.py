from django.contrib import admin
from django.contrib.admin import TabularInline
from carts.models import Cart, CartItem


class CartItemInline(TabularInline):
    model = CartItem
    fields = ("user", "product", "quantity")
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "ordered", "total_price"]
    inlines = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["id", "cart", "user", "product", "quantity"]
    fields = ("cart", "user", "product", "quantity")
