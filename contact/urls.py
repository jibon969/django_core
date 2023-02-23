from django.urls import path
from . import views

urlpatterns = [

    path('download-contact-csv/', views.download_contact_csv, name='download-contact-csv'),

]
