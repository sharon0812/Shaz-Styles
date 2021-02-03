from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.

class Image(models.Model):
    caption = models.CharField(max_length=100)
    title = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    price = models.CharField(max_length=200, default='')
    location = models.TextField(max_length=30,null=False,blank=False, default='')
    image=models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.caption

    class Meta:
        verbose_name='Images'
        
        
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    
class Category(models.Model):
    category = models.CharField(max_length=80, null= True)
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update()

    def __str__(self):
        return self.category
        
class categories(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
        
    def __str__(self):
        return self.name

class Avis(models.Model):
    note = models.IntegerField()