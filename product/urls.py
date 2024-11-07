from django.urls import include, path
from rest_framework.routers import DefaultRouter

from product.views import CreateProductView

router = DefaultRouter()  # amader router

router.register(r"", CreateProductView)  # router er antena
urlpatterns = [
    path("", include(router.urls)),
]
