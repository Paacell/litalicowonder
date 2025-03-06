from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages  # メッセージを追加
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    print("signup_1")
    if request.method == "POST":
        print("signup_2")
        form = CustomUserCreationForm(request.POST)
        print("signup_3")
        if form.is_valid():
            print("signup_4")
            user = form.save()
            print("signup_5")
            login(request, user)
            print("signup_6")
            return redirect("dashboard:home")
        else:
            print("signup_7")
            messages.error(request, "入力に誤りがあります。")
            print("signup_8")
    else:
        print("signup_9")
        form = CustomUserCreationForm()
        print("signup_10")
    return render(request, "accounts/signup.html", {"form": form})

def logout_view(request):
    print("logoutview_1")
    logout(request)
    print("logoutview_2")
    return redirect("accounts:login")

def login_view(request):
    print("login_1")
    form = AuthenticationForm(data=request.POST or None)  # フォームを作成
    print("login_2")
    if request.method == "POST":
        print("login_3")
        if form.is_valid():  # フォームのバリデーション
            print("login_4")
            user = form.get_user()
            print("login_5")
            login(request, user)
            print("login_6")
            return redirect("dashboard:home")
    print("login_7")
    return render(request, "accounts/login.html", {"form": form})

