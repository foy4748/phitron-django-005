from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from product.models import Product


# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviewed_products"
    )
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owned_reviews"
    )
    review_text = models.TextField(max_length=5048)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.review_text)[:20]} [20 chars only]"
