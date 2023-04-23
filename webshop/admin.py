from django.contrib import admin
from .models import Category, Print, Cart, CartItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Print)
admin.site.register(Cart)
admin.site.register(CartItem)
