from django.urls import path  # ,include

# from rest_framework.routers import DefaultRouter
from review.views import (
    CreateReviewView,
    DeleteReviewView,
    ProductSpecificReviewListView,
    ReviewListView,
    SingleReviewView,
    UpdateReviewView,
    UserAndProductSpecificReviewListView,
)


# router = DefaultRouter()  # amader router

# router.register(r"", CreateProductView)  # router er antena
urlpatterns = [
    # Review urls
    path("review-create/", CreateReviewView.as_view(), name="review_create"),
    path("review-update/<int:pk>/", UpdateReviewView.as_view(), name="review_update"),
    path("review-list/", ReviewListView.as_view(), name="review_list"),
    path(
        "product-review-list/",
        ProductSpecificReviewListView.as_view(),
        name="product_review_list",
    ),
    path(
        "product-user-review-list/",
        UserAndProductSpecificReviewListView.as_view(),
        name="product_user_review_list",
    ),
    path("review-detail/<pk>/", SingleReviewView.as_view(), name="review_detail"),
    path("review-delete/<pk>/", DeleteReviewView.as_view(), name="review_delete"),
    path("review-create/", CreateReviewView.as_view(), name="review_create"),
    path("review-update/<int:pk>/", UpdateReviewView.as_view(), name="review_update"),
]
