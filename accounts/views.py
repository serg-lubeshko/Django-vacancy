from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView

from accounts.forms import UserLoginForm, UserRegistryForm


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm(data=request.POST)
    return render(request, template_name="accounts/login.html", context={'form': form})


def register(request):
    if request.method == "POST":
        form = UserRegistryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request,"Ошибка регистрации")
    else:
        form = UserRegistryForm()
    return render(request, template_name="accounts/register.html", context={'form': form})


def user_logout(request):
    logout(request)
    return redirect("home")

