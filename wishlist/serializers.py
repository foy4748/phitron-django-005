from rest_framework import serializers

from wishlist.models import WishListItem


class WishItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListItem
        exclude = ("wish_item_owner",)


class WishItemCreateSerializer(serializers.ModelSerializer):
    wish_item_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = WishListItem
        fields = ["product", "wish_item_owner"]
