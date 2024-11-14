from rest_framework import serializers

from review.models import Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"

class ReviewUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['review_text','rating']
