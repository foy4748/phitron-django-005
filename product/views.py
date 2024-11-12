# from django.utils.http import urlsafe_base64_encode
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from product.models import Product, Review
from product.serializers import ProductSerializer, ProductUpdateSerializer, ReviewSerializer, ReviewUpdateSerializer
from rest_framework.response import Response
from utils.access_control import IsProductOwner, IsReviewOwner


# Create your views here.

# PRODUCT RELATED =============
class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class SingleProductView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class DeleteProductView(DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsProductOwner]
    queryset = Product.objects.all()


class UpdateProductView(UpdateAPIView):
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsAuthenticated, IsProductOwner]
    queryset = Product.objects.all()


# REVIEW RELATED =============
class ReviewListView(ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        data = Review.objects.filter(reviewer=self.request.user)
        return data


class SingleReviewView(RetrieveAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsReviewOwner]
    queryset = Review.objects.all()

    # def get_object(self):
    #     data = None
    #     data = get_object_or_404(
    #         Review,
    #         id=self.kwargs.get('pk'))
    #     # Checking Permission
    #     self.check_object_permissions(self.request, data)

    #     return data


class CreateReviewView(CreateAPIView):
    serializer_class = ReviewSerializer
    # queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]


class DeleteReviewView(DestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsReviewOwner]
    queryset = Review.objects.all()


class UpdateReviewView(UpdateAPIView):
    serializer_class = ReviewUpdateSerializer
    permission_classes = [IsAuthenticated, IsReviewOwner]
    queryset = Review.objects.all()
