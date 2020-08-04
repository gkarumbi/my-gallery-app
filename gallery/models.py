from django.db import models

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=255)
    image_location = models.ForeignKey('Location',on_delete=models.CASCADE)
    image_category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image= models.ImageField(upload_to='images/',null=True,blank=True)
    
    def __str__(self):
        return self.image_name

    
    def save_image(self):
        self.save()

    
    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.get(id = id)
        return image

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(categories__name__contains = search_term)
        return images

    @classmethod
    def filter_by_location(cls,search_term):
        location = Location.objects.get(name = search_term)
        images = cls.objects.filter(location = location)
        return images
        


class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category