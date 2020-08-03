from django.db import models

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=255)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)
    image= models.ImageField(upload_to='images/')

class Location(models.Model):
    location = models.CharField(max_length=30)


class Category(models.Model):
    category = models.CharField(max_length=30)