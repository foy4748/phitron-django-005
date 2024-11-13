from rest_framework import serializers

# from people.models import People
from people.serializers import UserListSerializer
from product.models import CartItem, Product, ProductCategory, Review

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
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"

class ReviewUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['review_text','rating']

# Cart Related
class CartItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        # depth = 1
        fields = "__all__"

class CartItemSerializer(serializers.ModelSerializer):

    cart_item_owner = UserListSerializer()
    class Meta:
        model = CartItem
        depth = 2
        fields = "__all__"

class CartItemUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['quantity']
