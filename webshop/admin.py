from django.contrib import admin
from .models import Category, Print, PrintOption

# Register your models here.
admin.site.register(Category)
admin.site.register(Print)
admin.site.register(PrintOption)

