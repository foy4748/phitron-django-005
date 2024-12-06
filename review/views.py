from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from review.serializers import (
    ReviewCreateSerializer,
    ReviewSerializer,
    ReviewUpdateSerializer,
)
from review.models import Review
from utils.access_control import IsReviewOwner


# Create your views here.
class ReviewListView(ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        data = Review.objects.filter(reviewer=self.request.user)
        return data


class ProductSpecificReviewListView(ListAPIView):
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["product"]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
    queryset = Review.objects.all()


class SingleReviewView(RetrieveAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsReviewOwner]

    def get_queryset(self):
        return Review.objects.filter(reviewer=self.request.user)

    # def get_object(self):
    #     data = None
    #     data = get_object_or_404(
    #         Review,
    #         id=self.kwargs.get('pk'))
    #     # Checking Permission
    #     self.check_object_permissions(self.request, data)

    #     return data


class CreateReviewView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
    # queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]


class DeleteReviewView(DestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsReviewOwner]

    def get_queryset(self):
        return Review.objects.filter(reviewer=self.request.user)


class UpdateReviewView(UpdateAPIView):
    serializer_class = ReviewUpdateSerializer
    permission_classes = [IsAuthenticated, IsReviewOwner]
    # queryset = Review.objects.all()

    def get_queryset(self):
        return Review.objects.filter(reviewer=self.request.user)
