from django.contrib.auth.models import User
from django.db import models

from product.models import Product

# Create your models here.


class WishListItem(models.Model):
    wish_item_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("wish_item_owner", "product")

    def __str__(self):
        return f"{self.wish_item_owner} - {self.product}"
