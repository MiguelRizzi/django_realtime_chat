from django.urls import path
from .views import (
    CustomLoginView,
    CustomLogoutView,
    CustomSignupView,
    AvatarDetailView,
    AvatarCreateView,
    AvatarUpdateView,
    AvatarDeleteView,
    AvatarConfirmDeleteView,
)
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("signup/", CustomSignupView.as_view(), name="signup"),
    path("avatar/<int:pk>/", AvatarDetailView.as_view(), name="avatar_detail"),
    path("avatar/create/", AvatarCreateView.as_view(), name="avatar_create"),
    path("avatar/update/<int:pk>/", AvatarUpdateView.as_view(), name="avatar_update"),
    path("avatar/confirm_delete/<int:pk>/", AvatarConfirmDeleteView.as_view(), name="avatar_confirm_delete"),
    path("avatar/delete/<int:pk>/", AvatarDeleteView.as_view(), name="avatar_delete"),
]