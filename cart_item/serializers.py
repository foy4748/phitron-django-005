from rest_framework import serializers

from cart_item.models import CartItem
from people.serializers import UserListSerializer


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        # depth = 1
        fields = ["product", "quantity"]

    def create(self, validated_data):
        product = validated_data.get("product")
        quantity = validated_data.get("quantity")
        if bool(quantity) is False:
            quantity = 1
        cart_item_owner = self.context["request"].user

        cart_item = CartItem.objects.create(
            product=product, quantity=quantity, cart_item_owner=cart_item_owner
        )
        return cart_item


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
