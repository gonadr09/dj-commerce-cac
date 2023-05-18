from django.urls import path
from .views import home, product_detail, order_list, order_detail

app_name = 'ecommerce'

urlpatterns = [
    path('', home, name='home'),
    path('product-detail/<int:id>/', product_detail, name='product-detail'),
    path('order-list/', order_list, name='order-list'),
    path('order-detail/', order_detail, name='order-detail')
]
