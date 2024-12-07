from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def landing_page(request):
    return render(request, 'Features/landing_page.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('')  # Replace 'quiz_home' with your quiz homepage URL name
        # else:
        #     messages.error(request, "Invalid username or password")
    return render(request, 'Features/login.html')

def register_view(request):
    if request.method == "POST":
        # Add logic for user registration
        return redirect('login_view')  # Redirect to login page after successful registration
    return render(request, 'Features/register.html')  # Render the registration form template
