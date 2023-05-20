from django.contrib import admin
from .models import Tag, Category, Product, Image, Order, OrderProduct 


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderProduct)