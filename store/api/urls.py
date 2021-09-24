from django.urls import path, include
from .views import ApiProductListView


urlpatterns = [

            path('list', ApiProductListView.as_view(), name="list"),

]