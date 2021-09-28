
from django.urls import path

from .views import  Error, order_placed, BasketView

app_name = 'payment'

urlpatterns = [
    path('', BasketView, name='basket'),
    path('orderplaced/', order_placed, name='order_placed'),
    path('error/', Error.as_view(), name='error'),
]