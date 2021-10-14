from django.urls import path, include
from .views import CheckDiscount, registration_view, ChangePasswordView, SetNewPasswordAPIView

urlpatterns = [
    path('discount', CheckDiscount.as_view(), name="discount"),
    path('register', registration_view, name="register"),
    path('changepassword', ChangePasswordView.as_view(), name="changepassword"),
    path('resetpassword', SetNewPasswordAPIView.as_view(), name="resetpassword"),


]