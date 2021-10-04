from django.urls import path, include
from .views import CheckDiscount

urlpatterns = [
    path('discount', CheckDiscount.as_view(), name="discount"),


]