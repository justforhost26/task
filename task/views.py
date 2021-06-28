from django.shortcuts import render

# Create your views here.
from task.models import WebsiteName, Sliders, Images, Menu, Footer


def index(request):
    data=WebsiteName.objects.all()
    id=data[0].id
    images=Images.objects.filter(website=id)
    sliders=Sliders.objects.filter(website=id)
    menus=Menu.objects.filter(website=id)
    footer=Footer.objects.get(website=id)
    return render(request,"index.html",{"datas":data,"images":images,"sliders":sliders,"menus":menus,"footer":footer})