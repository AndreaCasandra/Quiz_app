from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home_stdnt (request):
    return render(request, 'home_stdnt.html')

