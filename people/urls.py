from django.urls import path

from people import views


app_name = "people"

urlpatterns = [
    path("register/", views.UserRegistrationApiView.as_view(), name="register_people"),
]
