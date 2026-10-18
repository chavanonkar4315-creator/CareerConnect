from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, "accounts/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "username already exists.")
            return render(request, "accounts/register.html")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully!")

    return render(request, "accounts/register.html")


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            messages.success(request, "Login successful!")

            return redirect("dashboard")

        else:
            messages.error(request, "Invalid useername or password.")

    return render(request, "accounts/login.html")


@login_required
def dashboard(request):

    return render(request, "accounts/dashboard.html")

def user_logout(request):
    logout(request)

    messages.success(request, "You have been logged out.")

    return redirect("login")
# Create your views here.
