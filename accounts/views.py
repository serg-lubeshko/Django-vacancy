from django.contrib.auth import login
from django.shortcuts import render, redirect

from accounts.forms import UserLoginForm


def user_login(request):
    if request.method=="POST":
        form =  UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("home")
    else:
        form = UserLoginForm(data=request.POST)
    return render(request, template_name="accounts/login.html", context={'form': form})

def register(request):
    return render(request, template_name="accounts/register.html")