from .models import Product
from rest_framework import serializers
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk','name', 'content', 'price', 'get_discount')

