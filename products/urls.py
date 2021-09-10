from .views import *
from django.urls import path

app_name = 'products'

urlpatterns = [

    path('', store, name='store'),

]
