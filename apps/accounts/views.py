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
            # user = form.save(commit=False)  # Do not save to the database yet
            # user.first_name = form.cleaned_data['first_name']
            # user.last_name = form.cleaned_data['last_name']
            # user.username = f"{user.firstname}{user.lastname}"  # Combine first name and last name to create the username
            form.save()  # Save the user to the database

            print(f"User {User.username} signed up successfully.")

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
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)
            print(f"Attempting login with username: {email}")

            if user is not None:
                print("User {email} authenticated successfully.")
                login(request, user)
                request.session['email'] = user.email
                request.session['user_id'] = user.id
                return redirect('level_selection')  # Redirect to your desired URL after successful login
            else:
                print("Authentication failed for username: {email}")
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})
