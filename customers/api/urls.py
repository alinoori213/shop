from django.urls import path, include
from .views import registration_view, ChangePasswordView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    

]