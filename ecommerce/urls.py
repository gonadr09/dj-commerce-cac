from django.urls import path
from .views import index

app_name = 'ecommerce'

urlpatterns = [
    path('', index, name='home'),
]
