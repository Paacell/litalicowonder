app_name = "accounts"

from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import logout_view, login_view, signup

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
