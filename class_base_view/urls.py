from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("class-base-view/",
         TemplateView.as_view(template_name="class_base_view/class_base_view.html"),
         name="class-base-view"),
]
