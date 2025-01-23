# urls.py
from django.urls import path

from testing.views import (
    PaymentTesting,
    account_activation_email_preview,
    product_purchase_email_preview,
    test_protected_route,
)

urlpatterns = [
    # Payment testing
    path("payment-testing/", PaymentTesting.as_view(), name="test_payment_route"),
    # Email template testing
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
