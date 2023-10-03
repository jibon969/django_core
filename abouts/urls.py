from django.urls import path
from . import views

urlpatterns = [
    path("about-us/", views.about_us, name="about-us"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("asyncView/", views.AsyncView.as_view(), name="asyncView"),
    path("about-list/", views.AboutListView.as_view(), name="about-list"),
]
