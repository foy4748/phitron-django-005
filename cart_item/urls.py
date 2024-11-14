
from django.urls import path  # ,include
# from rest_framework.routers import DefaultRouter

from cart_item.views import CartItemListView, CreateCartItemView, DeleteCartItemView, UpdateCartItemView

urlpatterns = [

    # Cart Item urls
    path("cart-item-list/", CartItemListView.as_view(), name='cart__item_list'),
    path("cart-item-delete/<pk>/", DeleteCartItemView.as_view(),
         name='cart_item_delete'),
    path("cart-item-create/", CreateCartItemView.as_view(), name='cart_item_create'),
    path("cart-item-update/<int:pk>/",
         UpdateCartItemView.as_view(), name='cart_item_update'),
]
