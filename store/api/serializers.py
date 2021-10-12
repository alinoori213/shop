from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from store.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'image', 'slug', 'price', 'category']

