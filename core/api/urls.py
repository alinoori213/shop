from django.urls import path, include

urlpatterns = [
    path('orders/', include('orders.api.urls')),
    path('customers/', include('customers.api.urls')),
    path('products/', include('products.api.urls')),
    path('account/', include('account.api.urls')),
]
