from django.db import models

from django.contrib.auth.models import User
from product.models import Product

# Create your models here.

class CartItem(models.Model):
    cart_item_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # type: ignore
