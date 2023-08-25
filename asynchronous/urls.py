
from django.urls import path
from .views import sync_view, async_view

urlpatterns = [
    path("sync_view/", sync_view),
    path("async_view/", async_view)

]
