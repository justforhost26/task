from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
import manager
from task.models import WebsiteName, Menu, Sliders, Images, Footer


def manager_home(request):
   return render(request,"manager/manager_home.html")

def add_menu(request):
   data = WebsiteName.objects.all()
   if request.method=="POST":
      website=request.POST['website']
      name_of_nav_item=request.POST['name_of_nav_item']
      obj=WebsiteName.objects.get(name_of_website=website)
      website_id=obj.id
      if Menu.objects.filter(name_of_nav_item=name_of_nav_item,website_id=website_id).exists():
         messages.error(request,"Already Added")
         return redirect(add_menu)
      else:
         data = Menu(website=WebsiteName.objects.get(id=website_id),name_of_nav_item=name_of_nav_item,website_id=website_id)
         data.save()
         messages.success(request, "Add Successfullly")
         return redirect(add_menu)
   return render(request,"manager/add_menu.html",{"datas":data})

def add_sliders(request):
   data=WebsiteName.objects.all()
   if request.method=="POST":
      website=request.POST['website']
      Slider1=request.FILES['Slider1']
      Slider2=request.FILES['Slider2']
      Slider3=request.FILES['Slider3']
      obj=WebsiteName.objects.get(name_of_website=website)
      website_id=obj.id
      if Sliders.objects.filter(website_id=website_id).exists():
         messages.error(request,"Already Added")
         return redirect(add_sliders)
      else:
         data = Sliders(website=WebsiteName.objects.get(id=website_id),Slider1=Slider1,Slider2=Slider2,Slider3=Slider3,website_id=website_id)
         data.save()
         messages.success(request, "Add Successfullly")
         return redirect(add_sliders)
   return render(request,"manager/add_sliders.html",{"datas":data})

def add_images(request):
   data = WebsiteName.objects.all()
   if request.method=="POST":
      website=request.POST['website']
      image1=request.FILES['image1']
      image2=request.FILES['image2']
      image3=request.FILES['image3']
      image4 = request.FILES['image4']
      image5 = request.FILES['image5']
      image6 = request.FILES['image6']
      obj=WebsiteName.objects.get(name_of_website=website)
      website_id=obj.id
      if Images.objects.filter(website_id=website_id).exists():
         messages.error(request,"Already Added")
         return redirect(add_images)
      else:
         data = Images(website=WebsiteName.objects.get(id=website_id),image=image1,image2=image2,image3=image3,image4=image4,image5=image5,image6=image6)
         data.save()
         messages.success(request, "Add Successfullly")
         return redirect(add_images)
   return render(request,"manager/add_images.html",{"datas":data})

def add_footer(request):
   data = WebsiteName.objects.all()
   if request.method=="POST":
      website=request.POST['website']
      footer=request.FILES['footer']
      obj=WebsiteName.objects.get(name_of_website=website)
      website_id=obj.id
      if Footer.objects.filter(website_id=website_id).exists():
         messages.error(request,"Already Added")
         return redirect(add_footer)
      else:
         data = Footer(website=WebsiteName.objects.get(id=website_id),footer=footer)
         data.save()
         messages.success(request, "Add Successfullly")
         return redirect(add_footer)

   return render(request,"manager/add_footer.html",{"datas":data})


def add_websitename(request):
   if request.method=="POST":
      name_of_website=request.POST['name_of_website']
      if WebsiteName.objects.filter(name_of_website=name_of_website).exists():
         messages.error(request,"Already Added")
         return render(request, "manager/manager_home.html")
      else:
         data = WebsiteName(name_of_website=name_of_website)
         data.save()
         messages.success(request, "Add Successfullly")
         return render(request, "manager/manager_home.html")


def logout(request):
   return render(request,"manager_login.html")



