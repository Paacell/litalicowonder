# from django.urls import path
# from .views import signup, login_view, user_logout
# from django.contrib.auth import views as auth_views

app_name = "accounts"

# urlpatterns = [
#     path("login/", login_view, name="login"),
#     path("logout/", user_logout, name="logout"),
# ]


from django.urls import path
from django.contrib.auth.views import LoginView
from .views import logout_view, login_view, signup
from .views import register

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register"),
]
