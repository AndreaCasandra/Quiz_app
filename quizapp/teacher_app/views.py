from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

# quiz_home dashboard
def dashboard(request):
    return render(request, 'teacher_dashboard.html')