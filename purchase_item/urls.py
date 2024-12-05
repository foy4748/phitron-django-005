from django.urls import path
from purchase_item.views import PurchaseItemView, PurchasedItemListView


urlpatterns = [
    # path("login/", include(router.urls)),
    path("", PurchaseItemView, name="purchase_item"),
    path("list/", PurchasedItemListView.as_view(), name="purchase_item_list"),
]
