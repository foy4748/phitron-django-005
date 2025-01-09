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
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from product.models import Product, ProductCategory
from product.serializers import (
    ProductCategorySerializer,
    ProductCreateSerializer,
    ProductDetailSerializer,
    ProductSerializer,
    ProductUpdateSerializer,
)

# from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class ProductListPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = "limit"
    max_page_size = 50


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
    queryset = Product.objects.all().order_by("-created_at", "-updated_at")
    pagination_class = ProductListPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        "category": ["exact"],
        "unit_price": ["gte", "gt", "exact", "lt", "lte"],
    }
    search_fields = ["product_name", "description"]


class RandomProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("?")[:12]


class SingleProductView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


# User Specific
class UserSpecificProducts(ProductListView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Product.objects.filter(product_owner=self.request.user).order_by(
            "-created_at", "-updated_at"
        )
        return queryset


class DeleteProductView(DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsProductOwner]

    def get_queryset(self):
        queryset = Product.objects.filter(product_owner=self.request.user)
        return queryset


class UpdateProductView(UpdateAPIView):
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsAuthenticated, IsProductOwner]

    def get_queryset(self):
        queryset = Product.objects.filter(product_owner=self.request.user)
        return queryset


# Admin Specific
class AdminSpecificProducts(ProductListView):
    permission_classes = [IsAuthenticated, IsAdminUser]


class DeleteProductByAdminView(DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Product.objects.all()


class UpdateProductByAdminView(UpdateAPIView):
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Product.objects.all()
