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
        
# star rating
def avis(request, id): # view for displaying and storing the form
    commande = get_object_or_404(Commande, id=id)

    if request.method == "POST":
        form = AvisForm(request.POST)
        if form.is_valid():
            avis = form.save(commit = False)
            avis.commande = commande
            avis.save()
            commande.has_avis = True
            commande.save()
            if commande.plat.chef.nb_avis==0:
                commande.plat.chef.rating = avis.note
            else:
                commande.plat.chef.rating = (commande.plat.chef.rating*commande.plat.chef.nb_avis + avis.note)/(commande.plat.chef.nb_avis + 1)
            commande.plat.chef.nb_avis += 1
            commande.plat.chef.save()
            messages.success(request, 'Votre avis a été correctement envoyé !')
            return redirect(mes_commandes)
    else:
        form = AvisForm()

    return render(request, 'actualites/avis.html', locals())

def avis2(request, id): # view for recording the rating
    avis = get_object_or_404(Avis, id=id)
    rating = request.POST.get('rating')
    avis.note = rating
    avis.save()
    messages.success(request, 'Votre avis a été correctement envoyé !')
    return redirect(mes_commandes)