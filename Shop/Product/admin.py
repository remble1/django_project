from django.contrib import admin
from .models import Product

# Register your models here.

from .models import Product, Producent, Category

admin.site.register(Product)
admin.site.register(Producent)
admin.site.register(Category)