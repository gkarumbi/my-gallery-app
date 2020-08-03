from django.db import models

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=255)
    image_location = models.CharField(max_length=30)
    image_category = models.CharField(max_length = 30)
    image= models.ImageField(upload_to='images/')
