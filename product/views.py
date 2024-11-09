# from django.utils.http import urlsafe_base64_encode
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from product.models import Product, Review
from product.serializers import ProductSerializer, ReviewSerializer
from utils.access_control import IsOwner


# Create your views here.
class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class GetProductsView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# REVIEW RELATED =============
class ReviewListView(ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [ IsAuthenticated  ]

    def get_queryset(self):
        data = Review.objects.filter(reviewer=self.request.user.people_info)
        return data

class SingleReviewView(RetrieveAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [ IsAuthenticated, IsOwner  ]

    def get_object(self):
        data = Review.objects.get(reviewer=self.request.user.people_info,id=self.kwargs.get('pk'))
        print(data)
        return data

class CreateReviewView(CreateAPIView):
    serializer_class = ReviewSerializer
    # queryset = Review.objects.all()
    permission_classes = [ IsAuthenticated  ]

class UpdateReviewView(UpdateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [ IsAuthenticated  ]
