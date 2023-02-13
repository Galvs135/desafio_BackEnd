from django.urls import path
from . import views


urlpatterns = [
    path("file/", views.manage_file, name="file"),
    path("stores/", views.stores),
]