from rest_framework import serializers

from purchase_item.models import PurchasedItem
from review.models import Review

from rest_framework import serializers, status
from rest_framework.exceptions import APIException


class UnpurchasedProductReviewError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Logical error: The product has not been purchased."
    default_code = "logical_error"


class ReviewCreateSerializer(serializers.ModelSerializer):
    reviewer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = "__all__"

    def save(self, **kwargs):
        product = self.validated_data.get("product", None)
        purchased = PurchasedItem.objects.filter(product=product).first()

        if purchased is not None:
            return super().save(**kwargs)
        else:
            raise UnpurchasedProductReviewError()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["review_text", "rating"]
