from django.urls import path
from .views import (
    CustomLoginView,
    CustomLogoutView,
    CustomSignupView,
)
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("signup/", CustomSignupView.as_view(), name="signup"),
]