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
            request.session['user_full_name'] = f"{user.first_name} {user.last_name}"
            messages.success(request, f"Welcome {user.first_name} {user.last_name}! You have successfully signed up.")

            print(f"User {User.username} signed up successfully.")

            return redirect('accounts:login')  # Redirect to login page after successful signup
        else:
            # Print statement for unsuccessful signup
            print("Signup form is not valid. Errors:", form.errors)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    print("Login view accessed.")  # Debug statement
    if request.method == 'POST':
        print("POST request received.")  # Debug statement
        form = LoginForm(request, request.POST)
        if form.is_valid():
            print("Form is valid.")  # Debug statement
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(f"Form data - username: {username}, password: {password}")  # Debug statement

            user = authenticate(request, username=username, password=password)
            print(f"Attempting login with username: {username}")

            if user is not None:
                print(f"User {username} authenticated successfully.")
                login(request, user)
                request.session['email'] = user.email
                request.session['user_id'] = user.id
                return redirect('lessons:level_selection')  # Redirect to your desired URL after successful login
            else:
                print(f"Authentication failed for username: {username}")
                messages.error(request, 'Invalid username or password.')
        else:
            print("Form is not valid.")  # Debug statement
            print(form.errors)  # Debug statement to print form errors

        # Reset the form fields
        form = LoginForm()
    else:
        print("GET request received.")  # Debug statement
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})
