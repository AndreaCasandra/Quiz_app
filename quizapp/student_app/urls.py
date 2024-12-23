from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="students_dashboard"),
    path("user_dashboard/", views.user_dashboard, name="user_dashboard"),
]