from django.contrib import admin
from django.contrib import admin
from .models import Product, BasketItem, Order

# Register your models to appear in Django Admin
admin.site.register(Product)
admin.site.register(BasketItem)
admin.site.register(Order)


# Register your models here.
