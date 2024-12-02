from django.urls import path, include
from rest_framework.routers import DefaultRouter

from people import views


app_name = "people"

# router = DefaultRouter()  # amader router

# router.register(r"login", views.UserLoginView
# , basename='auth_api')  # router er antena
urlpatterns = [
    # path("login/", include(router.urls)),
    path("register/", views.UserRegistrationApiView.as_view(), name="register_people"),
    path("login/", views.UserLoginView.as_view(), name="login_people"),
    path("deposite/<pk>/", views.BalanceDepositeView.as_view(), name="update_balance"),
    path("", views.test_protected_route, name="test_protected_route"),
]
