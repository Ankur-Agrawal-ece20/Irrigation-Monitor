from django.urls import path
from .views import index, new_data

urlpatterns = [
    path("", index, name="index"),
    path("data", new_data, name="data"),
]