from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from store.models import Product
from .serializers import ProductSerializer


class ApiProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
