from django.shortcuts import render,redirect
from .models import Device
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.

def new_data(request, id):
    device = get_object_or_404(Device, device_id=id)
    data=request.data
    device.moisture_level.append(data['moisture_level'])
    if len(device.moisture_level)>50:
        device.moisture_level.pop(0)
    device.temperature.append(data['temperature'])
    if len(device.temperature)>50:
        device.temperature.pop(0)
    device.humidity.append(data['humidity'])
    if len(device.humidity)>50:
        device.humidity.pop(0)
    device.save()
    return JsonResponse({'status':'ok'})

def index(request):
    if request.user.is_authenticated is False:
        return redirect("/login")
    name=request.user.first_name
    username=request.user.username
    email=request.user.email
    devices=Device.objects.filter(user=request.user).count()
    return render(request, "user.html", {'name':name,'username':username,'email':email,'devices':devices})

def devices(request):
    if request.user.is_authenticated is False:
        return redirect("/login")
    devices=Device.objects.filter(user=request.user)
    return render(request, "devices.html", {'devices':devices})

def add_device(request,id):
    if request.user.is_authenticated is False:
        return redirect("/login")
    
    if Device.objects.filter(device_id=id).count()>0:
        return redirect("/devices")
    
    obj=[0 for i in range(0,5)]
    Device.objects.create(
        device_id=id, 
        user=request.user,
        moisture_level=obj,
        temperature=obj,
        humidity=obj,
        )

    return redirect("/devices")