from django.urls import path  # ,include

# from rest_framework.routers import DefaultRouter

from product.views import (
    AdminSpecificProducts,
    CategoryListView,
    CreateCategoryView,
    CreateProductView,
    DeleteProductByAdminView,
    DeleteProductView,
    ProductListView,
    RandomProductListView,
    SingleProductView,
    UpdateProductByAdminView,
    UpdateProductView,
    UserSpecificProducts,
)

# router = DefaultRouter()  # amader router

# router.register(r"", CreateProductView)  # router er antena
urlpatterns = [
    # Product urls
    path("", CreateProductView.as_view(), name="product_create"),
    path("product-list/", ProductListView.as_view(), name="product_list"),
    path(
        "random-product-list/",
        RandomProductListView.as_view(),
        name="random_product_list",
    ),
    path("product-detail/<pk>/", SingleProductView.as_view(), name="product_detail"),
    # User Specific
    path(
        "user-specific/product-list/",
        UserSpecificProducts.as_view(),
        name="user_specific_product_list",
    ),
    path("product-delete/<pk>/", DeleteProductView.as_view(), name="product_delete"),
    path(
        "product-update/<int:pk>/", UpdateProductView.as_view(), name="product_update"
    ),
    # Admin Specific
    path(
        "admin-specific/product-list/",
        AdminSpecificProducts.as_view(),
        name="admin_specific_product_list",
    ),
    path(
        "admin-specific/product-delete/<pk>/",
        DeleteProductByAdminView.as_view(),
        name="product_delete_by_admin",
    ),
    path(
        "admin-specific/product-update/<int:pk>/",
        UpdateProductByAdminView.as_view(),
        name="product_update_by_admin",
    ),
    # Category Related
    path("category-create/", CreateCategoryView.as_view(), name="category_create"),
    path("category-list/", CategoryListView.as_view(), name="category_list"),
]
