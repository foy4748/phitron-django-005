from django.db import models
from django.contrib.auth.models import User

from purchase_item.models import PurchasedItem
from transaction.constants import TRANSACTION_TYPE_CHOICES, PURCHASE


class Transaction(models.Model):
    purchased_product = models.ForeignKey(
        PurchasedItem,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="transaction_purchased_products",
    )
    type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
        default=PURCHASE,
    )
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    buyer = models.ForeignKey(
        User,
        related_name="buyer_transactions",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    seller = models.ForeignKey(
        User,
        related_name="seller_transactions",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.type} - {self.transaction_id}"
