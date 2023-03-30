from django.urls import path
from . import views

urlpatterns = [
    path('check-query-performance/', views.check_query_performance, name='check-query-performance'),
]
