from django.urls import path
from .views import index, new_data, devices, add_device, manual_mode, delete_device

urlpatterns = [
    path("", index, name="index"),
    path("data/<str:id>/<int:m>/<int:t>/<int:h>", new_data, name="data"),
    path("devices", devices, name="devices"),
    path("add_device/<str:id>", add_device, name="add_devices"),
    path("manual_mode/<str:id>", manual_mode, name="manual_mode"),
    path("delete_device/<str:id>", delete_device, name="delete_device"),
]