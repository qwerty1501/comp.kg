from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Category, Product, Image, ProductImage
from .serializers import CategorySerializers, ProductSerializers, ImageSerializers, ProductImageSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    
    
class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    
class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ImageListAPIView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers


class ImageRetrieveAPIView(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers


class ProductImageListAPIView(ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductImageRetrieveAPIView(RetrieveAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer