from django.urls import path, include
from .views import CheckDiscount, registration_view, ChangePasswordView

urlpatterns = [
    path('discount', CheckDiscount.as_view(), name="discount"),
    path('register', registration_view, name="register"),
    path('changepassword', ChangePasswordView.as_view(), name="changepassword"),


]