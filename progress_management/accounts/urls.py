app_name = "accounts"

from django.urls import path
from django.contrib.auth.views import LoginView
from .views import logout_view, login_view, signup
from .views import register

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
