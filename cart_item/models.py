from django.db import models

from django.contrib.auth.models import User
from product.models import Product

# Create your models here.


class CartItem(models.Model):
    cart_item_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, blank=True)  # type: ignore
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("cart_item_owner", "product")

    def __str__(self):
        return f"{self.cart_item_owner} - {self.product}"
