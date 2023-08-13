from django.urls import path
from . import views

urlpatterns = [
    path("restaurant-view/", views.RestaurantView.as_view(), name="restaurant-view"),
]