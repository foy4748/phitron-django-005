# urls.py
from django.urls import path

from testing.views import product_purchase_email_preview

urlpatterns = [
    path(
        "product-purchase-email-preview/",
        product_purchase_email_preview,
        name="product_purchase_preview",
    ),
]
