from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    else:
        return render(request, "users/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            messages.warning(request, "Invalid credential.")
            return render(request, "users/login.html", {
                "messages": messages.get_messages(request)
            })

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return render(request, "users/login.html", {
        "messages": messages.get_messages(request)
    })


def forget_password(request):
    return render(request, "users/forget-password.html")
