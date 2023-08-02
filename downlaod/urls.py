from django.urls import path
from . import views


urlpatterns = [
    path('download-csv/', views.download_csv, name='download-csv'),
    path('csv_database_write/', views.csv_database_write, name='csv_database_write'),

]
