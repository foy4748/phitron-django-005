from django.urls import path  # ,include
# from rest_framework.routers import DefaultRouter

from product.views import CreateProductView, CreateReviewView, DeleteReviewView, GetProductsView, ReviewListView, SingleReviewView, UpdateReviewView

# router = DefaultRouter()  # amader router

# router.register(r"", CreateProductView)  # router er antena
urlpatterns = [
    path("", CreateProductView.as_view(), name='product_create'),
    path("product-list/", GetProductsView.as_view(), name='product_list'),
    path("review-list/", ReviewListView.as_view(), name='review_list'),
    path("review-detail/<pk>/", SingleReviewView.as_view(),
         name='review_detail'),
    path("review-delete/<pk>/", DeleteReviewView.as_view(),
         name='review_delete'),
    path("review-create/", CreateReviewView.as_view(), name='review_create'),
    path("review-update/<int:pk>/",
         UpdateReviewView.as_view(), name='review_update'),
]
