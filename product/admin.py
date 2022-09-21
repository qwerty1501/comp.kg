from django.contrib import admin
from .models import Category, Product, ProductImage, Image


class ProductImageInlines(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInlines]


admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Product, ProductAdmin)