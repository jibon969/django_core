from django.urls import path
from . import views

urlpatterns = [
    path('add-student/', views.add_student, name="add-student"),
    path('add-student-form/', views.add_student_form, name="add-student-form"),
]
