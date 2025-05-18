from django.urls import path
from purchase_item.views import (
    CreatePaymentIntent,
    PurchaseItemView,
    PurchasedItemListView,
    PurchasedItemOrderListView,
)


urlpatterns = [
    # path("login/", include(router.urls)),
    path("list/", PurchasedItemListView.as_view(), name="purchase_item_list"),
    path(
        "order-list/",
        PurchasedItemOrderListView.as_view(),
        name="purchase_item_order_list",
    ),
    path(
        "create-payment-intent/",
        CreatePaymentIntent,
        name="create_purchase_item_payment_intent",
    ),
    path("payment/<str:transaction_id>/", PurchaseItemView, name="purchase_item"),
]
