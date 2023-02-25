from django.contrib import admin
from .models import CartItemShop, Product, WishList

admin.site.register(CartItemShop)
admin.site.register(Product)
admin.site.register(WishList)

