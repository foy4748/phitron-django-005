# from django.utils.http import urlsafe_base64_encode
from rest_framework.generics import CreateAPIView, ListAPIView

from product.models import Product, Review
from product.serializers import ProductSerializer, ReviewSerializer


# Create your views here.
class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class GetProductsView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CreateReviewView(CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
