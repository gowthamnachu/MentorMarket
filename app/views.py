from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from django.shortcuts import render


def become_mentor(request):
    return render(request, 'become_mentor.html')

def mentor_page(request):
    return render(request, 'mentor_page.html')

def career_mentor(request):
    return render(request, 'career_mentor.html')

def technical_mentor(request):
    return render(request, 'technical_mentor.html')

def life_mentor(request):
    return render(request, 'life_mentor.html')

def leadership_mentor(request):
    return render(request, 'leadership_mentor.html')

def entrepreneurship_mentor(request):
    return render(request, 'entrepreneurship_mentor.html')

def financial_mentor(request):
    return render(request, 'financial_mentor.html')

def health_mentor(request):
    return render(request, 'health_mentor.html')

def fitness_mentor(request):
    return render(request, 'fitness_mentor.html')

def nutrition_mentor(request):
    return render(request, 'nutrition_mentor.html')

def public_speaking_mentor(request):
    return render(request, 'public_speaking_mentor.html')

def writing_mentor(request):
    return render(request, 'writing_mentor.html')

def language_mentor(request):
    return render(request, 'language_mentor.html')

def design_mentor(request):
    return render(request, 'design_mentor.html')

def marketing_mentor(request):
    return render(request, 'marketing_mentor.html')

def intro_video(request):
    return render(request, 'intro_video.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')


@login_required  # Ensure user is logged in to access this page
def home(request):
    return render(request, 'home.html')

@login_required
def mentor(request):
    return render(request, 'mentor.html')

@login_required
def about(request):
    return render(request, 'about.html')

def home_view(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate form data
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, 'register.html')
def logout_view(request):
    logout(request)
    return redirect('login') 
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')  # Placeholder for a logged-in user's page
