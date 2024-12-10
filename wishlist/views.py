from django.shortcuts import render
from django_filters.filters import OrderingFilter
from rest_framework.exceptions import NotFound
from rest_framework.generics import DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from wishlist.models import WishListItem
from wishlist.serializers import WishItemSerializer

# Create your views here.


class WishItemListView(ListAPIView):
    serializer_class = WishItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        data = WishListItem.objects.filter(wish_item_owner=self.request.user)
        return data


class ProductSpecificWishItem(RetrieveAPIView):
    serializer_class = WishItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        product_pk = self.kwargs.get("pk")
        try:
            return WishListItem.objects.get(
                product_id=product_pk, wish_item_owner=self.request.user
            )
        except WishListItem.DoesNotExist:
            raise NotFound(detail="WishItem not found for this product and user.")


class WishItemDeleteView(DestroyAPIView):
    serializer_class = WishItemSerializer
    permission_classes = [IsAuthenticated]
