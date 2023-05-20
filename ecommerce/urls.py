from django.urls import path
from .views import Home, DetailProduct, product_detail, order_list, order_detail, error_404

app_name = 'ecommerce'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product-detail/<int:pk>/', DetailProduct.as_view(), name='product-detail'),
    path('order-list/', order_list, name='order-list'),
    path('order-detail/', order_detail, name='order-detail'),
]
