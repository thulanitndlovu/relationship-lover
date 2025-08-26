from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate


def user_register(request):
    # ...registration logic...
    if form.is_valid():
        # ...save user...
        return redirect('home')  # Replace 'home' with your actual home page url name
    return render(request), 'home/registration.html', {'form': form}

def login_or_register(request):
    return render(request, 'home/login_or_register.html')

def welcome(request):
    return render(request, 'home/welcome.html')

@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'home/profile_view.html', {'profile': profile})

@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated!")
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'home/profile_edit.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # or any protected page
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def index(request):
    return HttpResponse("Welcome to Lover Corner!")

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')  # Make sure 'login' is a valid URL name in your urls.py
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'home/signup.html', {'form': form})