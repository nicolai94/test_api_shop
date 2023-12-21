# from django.contrib import admin
# from django.contrib.admin import TabularInline
#
# from orders.models import Order
# from orders.models.orders import OrderProduct
#
#
# class OrderProductInline(TabularInline):
#     model = OrderProduct
#     extra = 1
#     fields = "__all__"
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = "__all__"
#     inlines = [OrderProductInline]
#
