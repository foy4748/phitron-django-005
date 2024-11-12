from django.urls import path  # ,include
# from rest_framework.routers import DefaultRouter

from product.views import CreateProductView, CreateReviewView, DeleteProductView, DeleteReviewView, ProductListView, ReviewListView, SingleProductView, SingleReviewView, UpdateProductView, UpdateReviewView

# router = DefaultRouter()  # amader router

# router.register(r"", CreateProductView)  # router er antena
urlpatterns = [
    # Product urls
    path("", CreateProductView.as_view(), name='product_create'),
    path("product-list/", ProductListView.as_view(), name='product_list'),
    path("product-detail/<pk>/", SingleProductView.as_view(),
         name='product_detail'),
    path("product-delete/<pk>/", DeleteProductView.as_view(),
         name='product_delete'),
    path("product-update/<int:pk>/",
         UpdateProductView.as_view(), name='product_update'),

    path("review-create/", CreateReviewView.as_view(), name='review_create'),
    path("review-update/<int:pk>/",
         UpdateReviewView.as_view(), name='review_update'),

    # Review urls
    path("review-list/", ReviewListView.as_view(), name='review_list'),
    path("review-detail/<pk>/", SingleReviewView.as_view(),
         name='review_detail'),
    path("review-delete/<pk>/", DeleteReviewView.as_view(),
         name='review_delete'),
    path("review-create/", CreateReviewView.as_view(), name='review_create'),
    path("review-update/<int:pk>/",
         UpdateReviewView.as_view(), name='review_update'),
]
