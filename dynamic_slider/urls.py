from django.urls import path
from . import views

urlpatterns = [
    path('dynamic-slider/', views.dynamic_slider, name="dynamic-slider")
]