from rest_framework import serializers

from product.serializers import ProductSerializer
from wishlist.models import WishListItem


class WishItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = WishListItem
        exclude = ("wish_item_owner",)


class WishItemCreateSerializer(serializers.ModelSerializer):
    wish_item_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = WishListItem
        fields = ["product", "wish_item_owner"]
