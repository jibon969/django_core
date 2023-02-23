from django.contrib import admin
from .models import Product, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_per_page = 20


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_per_page = 20

