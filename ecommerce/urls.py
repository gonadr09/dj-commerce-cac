from django.urls import path, include
from .views import index

app_name = 'ecommerce'

urlpatterns = [
    path('', index, name='index'),
]
