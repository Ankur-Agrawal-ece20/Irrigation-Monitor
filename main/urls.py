from django.urls import path
from .views import index, new_data, devices, add_device

urlpatterns = [
    path("", index, name="index"),
    path("data/<int:id>", new_data, name="data"),
    path("devices", devices, name="devices"),
    path("add_device/<int:id>", add_device, name="add_devices"),
]