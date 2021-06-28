"""craftin_images_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from manager import views

urlpatterns = [
    path('',views.manager_home,name="manager_home"),
    path('add_menu', views.add_menu, name="add_menu"),
    path('add_sliders', views.add_sliders, name="add_sliders"),
    path('add_images', views.add_images, name="add_images"),
    path('add_footer', views.add_footer, name="add_footer"),
    path('add_websitename', views.add_websitename, name="add_websitename"),
    path('logout', views.logout, name="logout"),

]
