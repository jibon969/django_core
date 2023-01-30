from django.urls import path
from . import views

urlpatterns = [
    path('student-list/', views.student_list, name="student-list")
]
