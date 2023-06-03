from django.contrib import admin
from .models import Tag, Category, Product, Image, Order, OrderProduct 


admin.site.register(Tag)
admin.site.register(Category)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category', 'stock', 'price'
    ]
    inlines = [ImageInline]


class PedidoItemInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created', 'status', 'total_price']
    inlines = [PedidoItemInline]
    readonly_fields = ['total_price']

    def total_price(self, obj):
        return obj.sum_total()

    total_price.short_description = 'Precio total'


#admin.site.register(OrderProduct)