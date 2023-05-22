from django.urls import path
from .views import Home, DetailProduct, ListProducts, category_products, tag_products, on_sales_products, order_list, order_detail

app_name = 'ecommerce'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('ecommerce/', ListProducts.as_view(), name='ecommerce'),
    path('ecommerce/product-detail/<int:pk>/', DetailProduct.as_view(), name='product-detail'),
    path('ecommerce/category/<slug:category_slug>', category_products, name='category'),
    path('ecommerce/tag/<slug:tag_slug>', tag_products, name='tag'),
    path('ecommerce/on-sales/', on_sales_products, name='on-sales'),
    path('order/list/', order_list, name='order-list'),
    path('order/detail/', order_detail, name='order-detail'),
    #buscador
]
