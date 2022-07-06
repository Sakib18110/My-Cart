from django.contrib import admin
from .models import Category, Product, Cart, Order, OrderItem, Profile

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(OrderItem)
