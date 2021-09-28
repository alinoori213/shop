from django.urls import path, include

urlpatterns = [
    path('orders/', include('orders.api.urls')),
    path('account/', include('account.api.urls')),
    path('store/', include('store.api.urls')),
]
