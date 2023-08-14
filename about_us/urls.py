from django.urls import path
from . import views

urlpatterns = [
    path("about-us/", views.about_us, name="about-us"),
]
