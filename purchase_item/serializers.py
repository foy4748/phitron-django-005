from rest_framework import serializers

from product.serializers import ProductSerializer
from purchase_item.models import PurchasedItem


class PurchasedItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = PurchasedItem
        fields = ["product", "unit_price", "unit_name", "quantity"]
