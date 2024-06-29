from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import User

def signup(request):
    if request.method == 'POST':
        # Sign up logic here
        pass
    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == 'POST':
        # Login logic here
        pass
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
