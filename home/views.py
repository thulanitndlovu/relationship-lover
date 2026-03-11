from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile
from .models import Profile

def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request, user)
        return redirect("welcome")

    return render(request, "register.html")

# Welcome page (no login needed)
def welcome(request):
    return render(request, 'home/welcome.html')

def index(request):
    return render(request, 'home/index.html')

# Main page (no login needed)
def main(request):
    return render(request, 'home/main.html')

# Signup page
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

# Login page
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})
# Logout
def user_logout(request):
    logout(request)
    return redirect('welcome')

# Profile view (no login required for now)
def profile_view(request):
    profile = getattr(request.user, 'profile', None)
    return render(request, 'home/profile_view.html', {'profile': profile})

# Profile edit (no login required for now)
def profile_edit(request):
    profile = getattr(request.user, 'profile', None)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated!")
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'home/profile_edit.html', {'form': form})

def browse_profiles(request):
    profiles = Profile.objects.all()
    return render(request, "home/browse.html", {"profiles": profiles})

def mainpage(request):
    return render(request, "home/main.html")


