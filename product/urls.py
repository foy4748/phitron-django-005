from django.urls import path  # ,include
# from rest_framework.routers import DefaultRouter

from product.views import CreateProductView, CreateReviewView, GetProductsView

# router = DefaultRouter()  # amader router

# router.register(r"", CreateProductView)  # router er antena
urlpatterns = [
    path("", CreateProductView.as_view(), name='product_create'),
    path("product-list/", GetProductsView.as_view(), name='product_list'),
    path("review-create/", CreateReviewView.as_view(), name='review_create'),
]
