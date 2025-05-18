from rest_framework import serializers

from people.serializers import UserListSerializer
from product.serializers import ProductSerializer
from purchase_item.models import PurchasedItem


class PurchasedItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    purchased_item_owner = UserListSerializer()

    class Meta:
        model = PurchasedItem
        fields = "__all__"
