from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import User  # Import your custom User model

def landing_page(request):
    return render(request, 'Features/landing_page.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate manually since you're not using hashed passwords
        try:
            user = User.objects.get(username=username, password=password)
            # Simulate a "login" by saving user info in the session
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            messages.success(request, "Successfully logged in!")
            return redirect(reverse('quiz_home'))  # Replace 'quiz_home' with your actual URL name
        except User.DoesNotExist:
            messages.error(request, "Invalid username or password.")
            return redirect(reverse('login_view'))

    return render(request, 'Features/login.html')

def register_view(request):
    if request.method == 'POST':
        user_type = request.POST.get('userType')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not user_type or not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect(reverse('register_view'))

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect(reverse('register_view'))

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect(reverse('register_view'))

        # Create the user
        user = User.objects.create(
            user_type=user_type,
            username=username,
            email=email,
            password=password,  # Password is saved as plain text
        )
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect(reverse('login_view'))
    
    return render(request, 'Features/register.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import User  # Import your custom User model

def landing_page(request):
    return render(request, 'Features/landing_page.html')


def register_view(request):
    if request.method == 'POST':
        user_type = request.POST.get('userType')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not user_type or not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect(reverse('register_view'))

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect(reverse('register_view'))

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect(reverse('register_view'))

        # Create the user
        user = User.objects.create(
            user_type=user_type,
            username=username,
            email=email,
            password=password,  # Password is saved as plain text
        )
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect(reverse('login_view'))
    
    return render(request, 'Features/register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate manually since you're not using hashed passwords
        try:
            user = User.objects.get(username=username, password=password)
            # Simulate a "login" by saving user info in the session
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            messages.success(request, "Successfully logged in!")
            return redirect(reverse('dashboard'))  # Replace 'quiz_home' with your actual URL name
        except User.DoesNotExist:
            messages.error(request, "Invalid username or password.")
            return redirect(reverse('login_view'))

    return render(request, 'Features/login.html')



# quiz_home dashboard
def dashboard(request):
    return render(request, 'Features/dashboard.html')

