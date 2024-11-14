from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView,  DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from utils.access_control import IsCartItemOwner

from cart_item.models import CartItem
from cart_item.serializers import CartItemCreateSerializer, CartItemSerializer, CartItemUpdateSerializer

# Create your views here.
class CartItemListView(ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated, IsCartItemOwner]

    def get_queryset(self):
        data = CartItem.objects.filter(cart_item_owner=self.request.user)
        return data


class CreateCartItemView(CreateAPIView):
    serializer_class = CartItemCreateSerializer
    # queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

class DeleteCartItemView(DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated, IsCartItemOwner]

    def get_queryset(self):
        return CartItem.objects.filter(cart_item_owner=self.request.user)


class UpdateCartItemView(UpdateAPIView):
    serializer_class = CartItemUpdateSerializer
    permission_classes = [IsAuthenticated, IsCartItemOwner]
    # queryset = Review.objects.all()

    def get_queryset(self):
        return CartItem.objects.filter(cart_item_owner=self.request.user)
