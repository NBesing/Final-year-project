# apps/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            username = f"{first_name}{last_name}"  # Combine first name and last name to create the username

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            print(f"User {username} signed up successfully.")


            return redirect('accounts:login')  # Redirect to login page after successful signup
        else:
            # Print statement for unsuccessful signup
            print("Signup form is not valid. Errors:", form.errors)

    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            print("Attempting login with username: {username}")

            if user is not None:
                print("User {username} authenticated successfully.")
                login(request, user)
                request.session['username'] = user.username
                request.session['user_id'] = user.id
                return redirect('lessons:level_selection')  # Redirect to your desired URL after successful login
            else:
                print("Authentication failed for username: {username}")
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})
