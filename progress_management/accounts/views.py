from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages  # メッセージを追加
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard:home")
        else:
            messages.error(request, "入力に誤りがあります。")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})

# def user_logout(request):
#     logout(request)
#     return redirect("accounts:login")  # ログアウト後にログインページへリダイレクト

def logout_view(request):
    logout(request)
    return redirect("accounts:login")

def login_view(request):
    form = AuthenticationForm(data=request.POST or None)  # フォームを作成
    if request.method == "POST":
        if form.is_valid():  # フォームのバリデーション
            user = form.get_user()
            login(request, user)
            return redirect("dashboard:home")
    return render(request, "accounts/login.html", {"form": form})