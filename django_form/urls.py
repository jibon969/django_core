from django.urls import path
from . import views

urlpatterns = [
    path('add-student/', views.add_student, name="add-student")
]
