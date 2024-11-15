# from django.utils.http import urlsafe_base64_encode
from utils.access_control import IsProductOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from product.models import Product
from product.serializers import (
    ProductCategorySerializer,
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


# PRODUCT RELATED =============


class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    # queryset = Product.objects.all()


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]


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
