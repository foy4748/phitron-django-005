from rest_framework import serializers

from review.models import Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    reviewer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        exclude = ("reviewer",)

    # def create(self, validated_data):
    #     product = validated_data.get("product")
    #     review_text = validated_data.get("review_text")
    #     rating = validated_data.get("rating")
    #     reviewer = self.context["request"].user

    #     review = Review.objects.create(
    #         product=product, review_text=review_text, rating=rating, reviewer=reviewer
    #     )
    #     return review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["review_text", "rating"]
