from django.db import models

# from people.models import People
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class ProductCategory(models.Model):
    category = models.CharField(max_length=2048)

class Product(models.Model):
    product_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owned_products")
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL,null=True)
    product_name = models.CharField(max_length=1024)
    image_url = models.URLField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    unit_name = models.CharField(max_length=128)
    description = models.CharField(max_length=5048)

    def __str__(self):
        return f"{self.product_name}"


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviewed_products")
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owned_reviews")
    review_text = models.TextField(max_length=5048)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{str(self.review_text)[:20]} [20 chars only]"


class CartItem(models.Model):
    cart_item_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # type: ignore
