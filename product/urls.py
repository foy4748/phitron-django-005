from django.urls import path  # ,include
# from rest_framework.routers import DefaultRouter

from product.views import CreateCategoryView, CreateProductView, DeleteProductView,  ProductListView, SingleProductView, UpdateProductView 

# router = DefaultRouter()  # amader router

# router.register(r"", CreateProductView)  # router er antena
urlpatterns = [
    # Product urls
    path("", CreateProductView.as_view(), name='product_create'),

    path("category-create/", CreateCategoryView.as_view(), name='category_create'),

    path("product-list/", ProductListView.as_view(), name='product_list'),
    path("product-detail/<pk>/", SingleProductView.as_view(),
         name='product_detail'),
    path("product-delete/<pk>/", DeleteProductView.as_view(),
         name='product_delete'),
    path("product-update/<int:pk>/",
         UpdateProductView.as_view(), name='product_update'),

]
