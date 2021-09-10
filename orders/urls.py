from .views import *
from django.urls import path

app_name = 'orders'

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),

]
