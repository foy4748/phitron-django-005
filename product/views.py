from django.utils.http import urlsafe_base64_encode
from rest_framework import viewsets

from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.
class CreateProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
