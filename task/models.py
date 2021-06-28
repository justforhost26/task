from django.db import models

# Create your models here.
from django.db.models import Model


class WebsiteName(Model):
    name_of_website=models.CharField(max_length=500)
    def __str__(self):
        return self.name_of_website

class Menu(Model):
    website=models.ForeignKey(WebsiteName,on_delete=models.CASCADE)
    name_of_nav_item=models.CharField(max_length=500)
    def __str__(self):
        return self.name_of_nav_item

class Sliders(Model):
    website = models.ForeignKey(WebsiteName,on_delete=models.CASCADE)
    Slider1 = models.ImageField(upload_to='static/slider_image/',default="static/default.jpg")
    Slider2 = models.ImageField(upload_to='static/slider_image/',default="static/default.jpg")
    Slider3 = models.ImageField(upload_to='static/slider_image/',default="static/default.jpg")

class Images(Model):
    website=models.ForeignKey(WebsiteName,on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='static/images/', default="static/default.jpg")
    image2 = models.ImageField(upload_to='static/images/', default="static/default.jpg")
    image3 = models.ImageField(upload_to='static/images/', default="static/default.jpg")
    image4 = models.ImageField(upload_to='static/images/', default="static/default.jpg")
    image5 = models.ImageField(upload_to='static/images/', default="static/default.jpg")
    image6 = models.ImageField(upload_to='static/images/', default="static/default.jpg")

class Footer(Model):
    website = models.ForeignKey(WebsiteName, on_delete=models.CASCADE)
    footer = models.ImageField(upload_to='static/footer_images/', default="static/default.jpg")

class ManagerLogin(Model):
    userid=models.CharField(max_length=520)
    password=models.CharField(max_length=250)
    def __str__(self):
        return self.userid