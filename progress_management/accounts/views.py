# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm
# from django.contrib import messages  # メッセージを追加
# from django.contrib.auth.forms import AuthenticationForm
# import logging

# logger = logging.getLogger(__name__)

# def signup(request):
#     logger.debug("signup_1")
#     if request.method == "POST":
#         logger.debug("signup_2")
#         form = CustomUserCreationForm(request.POST)
#         logger.debug("signup_3")
#         if form.is_valid():
#             logger.debug("signup_4")
#             user = form.save()
#             logger.debug("signup_5")
#             login(request, user)
#             logger.debug("signup_6")
#             return redirect("dashboard:home")
#         else:
#             logger.debug("signup_7")
#             messages.error(request, "入力に誤りがあります。")
#             logger.debug("signup_8")
#     else:
#         logger.debug("signup_9")
#         form = CustomUserCreationForm()
#         logger.debug("signup_10")
#     return render(request, "accounts/signup.html", {"form": form})

# def logout_view(request):
#     logger.debug("logoutview_1")
#     logout(request)
#     logger.debug("logoutview_2")
#     return redirect("accounts:login")

# def login_view(request):
#     logger.debug("login_1")
#     form = AuthenticationForm(data=request.POST or None)  # フォームを作成
#     logger.debug("login_2")
#     if request.method == "POST":
#         logger.debug("login_3")
#         if form.is_valid():  # フォームのバリデーション
#             logger.debug("login_4")
#             user = form.get_user()
#             logger.debug("login_5")
#             login(request, user)
#             logger.debug("login_6")
#             return redirect("dashboard:home")
#     logger.debug("login_7")
#     return render(request, "accounts/login.html", {"form": form})

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages  # メッセージを追加
from django.contrib.auth.forms import AuthenticationForm
import logging

logger = logging.getLogger(__name__)

def signup(request):
    logger.debug("signup_1")
    if request.method == "POST":
        logger.debug("signup_2")
        form = CustomUserCreationForm(request.POST)
        logger.debug("signup_3")
        if form.is_valid():
            logger.debug("signup_4")
            user = form.save()
            logger.debug("signup_5")
            login(request, user)
            logger.debug("signup_6")
            return redirect("dashboard:home")
        else:
            logger.debug("signup_7")
            messages.error(request, "入力に誤りがあります。")
            logger.debug("signup_8")
    else:
        logger.debug("signup_9")
        form = CustomUserCreationForm()
        logger.debug("signup_10")
    return render(request, "accounts/signup.html", {"form": form})

def logout_view(request):
    logger.debug("logoutview_1")
    logout(request)
    logger.debug("logoutview_2")
    return redirect("accounts:login")

def login_view(request):
    logger.debug("login_1")
    form = AuthenticationForm(data=request.POST or None)  # フォームを作成
    logger.debug("login_2")
    if request.method == "POST":
        logger.debug("login_3")
        if form.is_valid():  # フォームのバリデーション
            logger.debug("login_4")
            user = form.get_user()
            logger.debug("login_5")
            login(request, user)
            logger.debug("login_6")
            return redirect("dashboard:home")
    logger.debug("login_7")
    return render(request, "accounts/login.html", {"form": form})
