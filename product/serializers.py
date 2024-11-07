from rest_framework import serializers

# from people.models import People
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    # product_owner = serializers.PrimaryKeyRelatedField(
    #     queryset=People.objects.all())

    class Meta:
        model = Product
        fields = "__all__"
