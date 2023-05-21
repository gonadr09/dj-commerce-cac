from django.urls import path
from .views import add_to_cart, subtract_from_cart, remove_from_cart, clear_cart

app_name="cart"

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add'),
    path('subtract/<int:product_id>/', subtract_from_cart, name='subtract'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove'),
    path('clear/', clear_cart, name='clear'),
]
