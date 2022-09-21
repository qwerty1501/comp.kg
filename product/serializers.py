from rest_framework import serializers
from .models import Category, Product, Image, ProductImage


class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name', )
        
        
class ProductSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id', 'image', 'name', 'discriptions', 'price', 'category')


class ImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('name', 'image')


class ProductImageSerializer(serializers.ModelSerializer):
    images = ImageSerializers()

    class Meta:
        model = ProductImage
        fields = '__all__'