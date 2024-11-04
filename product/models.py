from django.db import models

from people.models import People
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Product(models.Model):
    product_owner = models.ForeignKey(People, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=1024)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    unit_name = models.CharField(max_length=128)
    description = models.CharField(max_length=5048)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=5048)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )


class Cart(models.Model):
    cart_owner = models.ForeignKey(People, on_delete=models.CASCADE)
    product_count = models.PositiveIntegerField(default=0)  # type: ignore
    total_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # type: ignore
