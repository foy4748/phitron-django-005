from django.urls import path

from wishlist.views import (
    ProductSpecificWishItem,
    WishItemCreateView,
    WishItemDeleteView,
    WishItemListView,
)  # ,include

urlpatterns = [
    # Review urls
    path("create/", WishItemCreateView.as_view(), name="wishitem_create"),
    path("list/", WishItemListView.as_view(), name="wishitem_list"),
    path(
        "detail/<pk>/",
        ProductSpecificWishItem.as_view(),
        name="wishitem_detail",
    ),
    path("delete/<pk>/", WishItemDeleteView.as_view(), name="wishitem_delete"),
]
