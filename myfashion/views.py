from django.shortcuts import render
from .models import Image
from django.db import models

# Create your views here.

def welcome(request):
   title= 'Here are the services we offer'
   images = Image.objects.all()
   return render(request, 'myfashion/home.html', {'title' :title, 'images':images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'myfashion/search.html',{"message":message,"images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'myfashion/search.html', {"message": message})

        
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    
