# urls.py
from django.urls import path

from testing.views import (
    account_activation_email_preview,
    product_purchase_email_preview,
    test_protected_route,
)

urlpatterns = [
    path(
        "product-purchase-email-preview/",
        product_purchase_email_preview,
        name="product_purchase_preview",
    ),
    path(
        "account-activation-email-preview/",
        account_activation_email_preview,
        name="account_activation_preview",
    ),
    path("", test_protected_route, name="test_protected_route"),
]
