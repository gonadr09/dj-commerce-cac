from django.urls import path
from .views import index
from .views import compra

app_name = 'ecommerce'

urlpatterns = [
    path('', index, name='index'),
    path('compra', compra, name='compra')
]
