from django.db import models

# from people.models import People
from django.contrib.auth.models import User


# Create your models here.
class ProductCategory(models.Model):
    category = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    product_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owned_products"
    )
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=1024)
    image_url = models.URLField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    unit_name = models.CharField(max_length=128)
    description = models.CharField(max_length=5048)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name}"
