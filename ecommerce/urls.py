from django.urls import path
from .views import home, detail

app_name = 'ecommerce'

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:id>/', detail, name='detail')
]
