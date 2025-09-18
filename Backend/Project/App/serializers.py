from rest_framework import serializers
from .models import Shop, WebContent, Category, Product

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class WebContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=WebContent
        fields='__all__'
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
