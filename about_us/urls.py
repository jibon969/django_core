from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("about/", views.about_us, name="about"),
    path("about-us/", views.AboutUs.as_view(), name="about-us"),
    path("about-us-view/", views.AboutUsView.as_view(), name="about-us-view"),
    path("help/", TemplateView.as_view(template_name="about_us/help.html")),
]
