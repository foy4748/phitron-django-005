from django.urls import path

from wishlist.views import (
    ProductSpecificWishItem,
    WishItemDeleteView,
    WishItemListView,
)  # ,include

urlpatterns = [
    # Review urls
    path("wishitem-create/", WishItemListView.as_view(), name="wishitem_create"),
    path(
        "wishitem-detail/<pk>/",
        ProductSpecificWishItem.as_view(),
        name="wishitem_detail",
    ),
    path("wishitem-delete/<pk>/", WishItemDeleteView.as_view(), name="wishitem_delete"),
]
