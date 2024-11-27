from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
  list_display = ['name', 'phone', 'email', 'address']

class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'rate']

class OrderAdmin(admin.ModelAdmin):
  list_display = ['customer', 'status']

class OrderItemAdmin(admin.ModelAdmin):
  list_display = ['order', 'product', 'quantity', 'price']

admin.site.register(Customer,  CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)