from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Class, Quiz  # Import the models

def dashboard(request):
    # Retrieve classes and quizzes for the logged-in teacher
    classes = Class.objects.filter(teacher=request.user)  # Ensure 'teacher' is a valid field
    quizzes = Quiz.objects.filter(assigned_class__teacher=request.user)  # Ensure the relationship exists
    return render(request, 'teacher_dashboard.html', {'classes': classes, 'quizzes': quizzes})

def create_class(request):
    return HttpResponse("Create Class Page")

def create_quiz(request):
    return HttpResponse("Create Quiz Page")

def manage_class(request, class_id):
    return HttpResponse(f"Manage Class Page for Class ID {class_id}")

def view_results(request, quiz_id):
    return HttpResponse(f"View Results Page for Quiz ID {quiz_id}")
