from django.urls import path
from .views import Home, DetailProduct, ListProducts, category_products, tag_products, on_sales_products, order_create, DetailOrder, ListOrder

app_name = 'ecommerce'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('ecommerce/', ListProducts.as_view(), name='ecommerce'),
    path('ecommerce/product-detail/<int:pk>/', DetailProduct.as_view(), name='product-detail'),
    path('ecommerce/category/<slug:category_slug>', category_products, name='category'),
    path('ecommerce/tag/<slug:tag_slug>', tag_products, name='tag'),
    path('ecommerce/on-sales/', on_sales_products, name='on-sales'),
    path('order/create/', order_create, name='order-create'),
    path('order/list/', ListOrder.as_view(), name='order-list'),
    path('order/detail/<int:pk>/', DetailOrder.as_view(), name='order-detail'),
]
