from django.urls import path
from purchase_item.views import PurchaseItemView


urlpatterns = [
    # path("login/", include(router.urls)),
    path("", PurchaseItemView, name="purchase_item"),
]
