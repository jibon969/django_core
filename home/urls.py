from django.views.generic.base import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('', TemplateView.as_view(template_name='home/home.html')),
    path('home/', views.home, name="home"),
    path('homeView/', views.Home.as_view(), name="homeView"),
]
