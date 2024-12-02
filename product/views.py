# from django.utils.http import urlsafe_base64_encode
from utils.access_control import IsProductOwner
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from product.models import Product, ProductCategory
from product.serializers import (
    ProductCategorySerializer,
    ProductCreateSerializer,
    ProductDetailSerializer,
    ProductSerializer,
    ProductUpdateSerializer,
)

# from rest_framework.response import Response


# Create your views here.


class CreateCategoryView(CreateAPIView):
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAuthenticated]
    # queryset = Product.objects.all()


class CategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


# PRODUCT RELATED =============


class CreateProductView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]
    # queryset = Product.objects.all()


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        "category": ["exact"],
        "unit_price": ["gte", "gt", "exact", "lt", "lte"],
    }
    search_fields = ["product_name", "description"]


class SingleProductView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


class DeleteProductView(DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsProductOwner]
    queryset = Product.objects.all()


class UpdateProductView(UpdateAPIView):
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsAuthenticated, IsProductOwner]
    queryset = Product.objects.all()
