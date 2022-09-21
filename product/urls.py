from django.urls import path

from .views import CategoryListAPIView, CategoryRetrieveAPIView, ProductListAPIView, ProductRetrieveAPIView, ImageListAPIView, ImageRetrieveAPIView, ProductImageListAPIView, ProductImageRetrieveAPIView

urlpatterns = [
    # Category
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveAPIView.as_view()),
    # Product
    path('product/', ProductListAPIView.as_view()),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view()),
    # Images
    path('image/', ImageListAPIView.as_view()),
    path('image/<int:pk>/', ImageRetrieveAPIView.as_view()),
    # ProductImage
    path('prod-img/', ProductImageListAPIView.as_view()),
    path('prod-img/<int:pk>/', ProductImageRetrieveAPIView.as_view())
]