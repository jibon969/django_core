from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("about-us/", views.about_us, name="about-us"),
    path("aboutUs/", views.AboutUs.as_view(), name="aboutUs"),
    path("aboutUsView/", views.AboutUsView.as_view(), name="aboutUsView"),
    path("help/", TemplateView.as_view(template_name="about_us/help.html")),
]
