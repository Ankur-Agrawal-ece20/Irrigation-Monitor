from django.shortcuts import render,redirect
from .models import Device
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.

def new_data(request, device_id):
    device = get_object_or_404(Device, device_id=device_id)
    data=request.data
    device.moisture_level.append(data['moisture_level'])
    device.temperature.append(data['temperature'])
    device.humidity.append(data['humidity'])
    device.save()
    return JsonResponse({'status':'ok'})

def index(request):
    if request.user.is_authenticated is False:
        return redirect("/login")
    devices = Device.objects.filter(user=request.user)
    name=request.user.username
    return render(request, 'index.html', {'devices': devices})
