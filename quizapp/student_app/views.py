from django.shortcuts import render

# Create your views here.
# quiz_home dashboard
def dashboard(request):
    return render(request, 'student_dashboard.html')

def user_dashboard(request):
    return render(request, 'user_dashboard.html')


