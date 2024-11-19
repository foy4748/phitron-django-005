from rest_framework import serializers

# from people.models import People
from people.serializers import UserListSerializer
from product.models import Product, ProductCategory


# Product Related
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    # Thanks to this StackOverFlow page
    # https://stackoverflow.com/questions/54921401/django-rest-framework-how-to-associate-the-object-with-the-user-when-posting-th
    product_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductDetailSerializer(serializers.ModelSerializer):
    product_owner = UserListSerializer()
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("id", "product_owner")


# Review Related

# Cart Related
