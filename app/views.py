from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages

def homepage(request):
    return render(request, 'homepage.html')

    


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # Validate the inputs
        if not name or not email or not password:
            messages.error(request, 'All fields are required.')
            return render(request, 'register.html')

        # Check if the user already exists by email or username
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exists.')
            return render(request, 'register.html')

        if User.objects.filter(username=name).exists():
            messages.error(request, 'Username already taken. Please choose a different username.')
            return render(request, 'register.html')

        # Create the User
        user = User.objects.create_user(username=name, email=email, password=password)

        # Check if UserProfile already exists
        UserProfile.objects.get_or_create(user=user, defaults={'mobile': mobile, 'user_type': user_type})

        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')  # Redirect to the login page

    return render(request, 'register.html')
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserProfile  # Import your UserProfile model if needed

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Use email for authentication
        password = request.POST.get('password')

        # Authenticate using username (which defaults to the User's username field)
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')

            # Redirect based on user type
            user_profile = UserProfile.objects.get(user=user)
            if user_profile.user_type == 'vendor':
                return redirect('dashboard_ven')
            elif user_profile.user_type == 'businessman':
                return redirect('dashboard_bus')
            elif user_profile.user_type == 'person':
                return redirect('dashboard_pers')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')  # Adjust to your template path


def dashboard_bus(request):
    return "buss"
def dashboard_pers(request):
    return "ven"
def dashboard_ven(request):
    return "comp"


def contact(request):
    return None