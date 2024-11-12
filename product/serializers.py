from rest_framework import serializers

# from people.models import People
from product.models import Product, Review


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('id','product_owner')


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"

class ReviewUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['review_text','rating']
