from rest_framework import serializers

from wishlist.models import WishListItem


class WishItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListItem
        exclude = ("wish_item_owner",)
