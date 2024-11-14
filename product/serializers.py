from rest_framework import serializers

# from people.models import People
from product.models import Product, ProductCategory

# Product Related
class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('id','product_owner')


# Review Related

# Cart Related
