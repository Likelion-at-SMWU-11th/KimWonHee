from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm, SignUpForm


def logout_view(request):
    # 데이터 유효성 검사
    if request.user.is_authenticated:
        logout(request)
        # 비즈니스 로직 처리-로그아웃
    return redirect("index")


def login_view(request):
    # get, post 분리
    if request.method == "GET":
        return render(request, "accounts/login.html", {"form": AuthenticationForm()})
    else:
        # 데이터 유효성 검사
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 비즈니스 로직 처리: 로그인 처리
            login(request, form.user_cache)
            # 응답
            return redirect("index")
        else:
            # 비즈니스 로직 처리- 로그인 실패
            # 응답
            return render(request, "accounts/login.html", {"form": form})


# Create your views here.
def signup_view(request):
    if request.method == "GET":
        form = SignUpForm
        context = {"form": form}
        return render(request, "accounts/signup.html", context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect("index")
        else:
            return redirect("accounts:signup")
