from django.urls import path
from . import views

urlpatterns = [
    path('add-student/', views.add_student, name="add-student"),
    path('add-student-form/', views.add_student_form, name="add-student-form"),
    path('student_create_form/', views.student_create_form, name="student_create_form"),
    path('restaurant_create/', views.restaurant_create, name='restaurant_create'),
]
