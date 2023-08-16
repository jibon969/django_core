from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('homeView/', views.Home.as_view(), name="homeView"),
]