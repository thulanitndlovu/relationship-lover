from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile, Like, Message

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
def view_profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    return render(request, "home/view_profile.html", {"profile": profile})

# Profile edit (no login required for now)
def profile_edit(request):
    profile = getattr(request.user, 'profile', None)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
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

def browse_profiles(request):
    search = request.GET.get("search")

    if search:
        profiles = Profile.objects.filter(
            user__username__icontains=search
        ) | Profile.objects.filter(
            location__icontains=search
        )
    else:
        profiles = Profile.objects.all()

    return render(request, "home/browse.html", {"profiles": profiles})

def like_profile(request, id):
    receiver = get_object_or_404(User, id=id)
    sender = request.user

    if sender != receiver:
        Like.objects.get_or_create(sender=sender, receiver=receiver)

    return redirect("browse")

def send_message(request, id):
    receiver = get_object_or_404(User, id=id)
    sender = request.user

    if request.method == "POST":
        message_text = request.POST.get("message")

        if message_text:
            Message.objects.create(
                sender=sender,
                receiver=receiver,
                message=message_text
            )

        return redirect("browse")

    return render(request, "home/message.html", {"receiver": receiver})
