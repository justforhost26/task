from django.contrib import messages
from django.shortcuts import render

from task.models import ManagerLogin



def manager_login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        if ManagerLogin.objects.filter(userid=userid,password=password).exists():
            messages.success(request,"login Success")
            return render(request,"manager/manager_home.html")
        else:
            messages.error(request, "login failed")
            return render(request, "manager_login.html")
    return render(request,"manager_login.html")
