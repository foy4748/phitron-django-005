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
    path("logout/", views.LogOutView.as_view(), name="logout_people"),
    path("deposite/", views.BalanceDepositeView.as_view(), name="update_balance"),
    path("balance/", views.BalanceCheckView.as_view(), name="check_balance"),
    path(
        "change-password/", views.ChangePasswordView.as_view(), name="change_password"
    ),
    path("active/<uid64>/<token>/", views.activate, name="activate_people"),
]
