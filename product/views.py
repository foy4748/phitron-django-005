# from django.utils.http import urlsafe_base64_encode
from rest_framework.generics import CreateAPIView, ListAPIView

from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.
class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class GetProductsView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
