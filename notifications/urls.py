from django.urls import path
from . import views

urlpatterns = [
    path('notification/', views.notification_list, name="notification"),
    path('delete-notification/<int:id>/', views.delete_notification, name="delete-notification"),
]
