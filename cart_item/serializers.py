from rest_framework import serializers

from cart_item.models import CartItem
from people.serializers import UserListSerializer


class CartItemCreateSerializer(serializers.ModelSerializer):
    cart_item_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    quantity = serializers.IntegerField(default=1)

    class Meta:
        model = CartItem
        # depth = 1
        fields = ["product", "quantity", "cart_item_owner"]


class CartItemSerializer(serializers.ModelSerializer):
    cart_item_owner = UserListSerializer()

    class Meta:
        model = CartItem
        depth = 1
        fields = "__all__"


class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["quantity"]
