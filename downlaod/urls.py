from django.urls import path
from . import views


urlpatterns = [
    path('download-csv/', views.download_csv, name='download-csv'),
    path('downlaod-model-field-csv/', views.downlaod_model_field_csv, name='downlaod-model-field-csv'),

]
