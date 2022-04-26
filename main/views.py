from django.shortcuts import render,redirect
from .models import Device
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def new_data(request, id, m, t, h):
    device = get_object_or_404(Device, device_id=id)
    device.moisture_level.append(min(150,m))
    while len(device.moisture_level)>50:
        device.moisture_level.pop(0)
    device.temperature.append(min(150,t))
    while len(device.temperature)>50:
        device.temperature.pop(0)
    device.humidity.append(min(150,h))
    while len(device.humidity)>50:
        device.humidity.pop(0)
    device.save()
    if device.manual_mode:
        return JsonResponse({'status':'false','message':'Manual Mode'}, status=300)
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
    
    obj=[0 for i in range(0,50)]
    Device.objects.create(
        device_id=id, 
        user=request.user,
        manual_mode=False,
        moisture_level=obj,
        temperature=obj,
        humidity=obj,
        )

    return redirect("/devices")

def manual_mode(request,id):
    if request.user.is_authenticated is False:
        return redirect("/login")
    
    device = get_object_or_404(Device, device_id=id)
    device.manual_mode=not device.manual_mode
    device.save()
    return redirect("/devices")

def delete_device(request,id):
    if request.user.is_authenticated is False:
        return redirect("/login")
    
    device = get_object_or_404(Device, device_id=id)
    device.delete()
    return redirect("/devices")