from django.contrib.auth.models import User
from django.db import models

from product.models import Product


# Create your models here.
class PurchasedItem(models.Model):
    purchased_item_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    unit_name = models.CharField(max_length=128)

    quantity = models.PositiveIntegerField(default=1, blank=True)  # type: ignore
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.purchased_item_owner} - {self.product}"
