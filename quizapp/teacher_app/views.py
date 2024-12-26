from django.shortcuts import render, redirect
from django.http import HttpResponse

def dashboard(request):
    return render(request, 'teacher_dashboard.html')

def create_class(request):
    return HttpResponse("Create Class Page")

def create_quiz(request):
    return HttpResponse("Create Quiz Page")

def manage_class(request, class_id):
    return HttpResponse(f"Manage Class Page for Class ID {class_id}")

def view_results(request, quiz_id):
    return HttpResponse(f"View Results Page for Quiz ID {quiz_id}")
