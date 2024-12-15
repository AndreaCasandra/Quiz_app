from django.shortcuts import render

# Create your views here.


def home_tchrs(request):
    return render(request, 'home_tchrs.html')

