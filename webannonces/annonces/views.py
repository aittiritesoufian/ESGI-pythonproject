from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User
from annonces.models import Annonceur, Annonces
from .forms import InscriptionForm
import random
import pickle


def home(request):
    return render(request, 'annonces/home.html')

def getAnnonce(request, id_annonce):
    annonce = Annonces.objects.get(id=id_annonce)

    if(annonce is None):
        return redirect(home)
    return render(request, 'annonces/annonce.html', locals())

def list(request):
    annonces = Annonces.objects.all().order_by('date')
    return render(request, 'annonces/list-annonces.html', locals())

def listSearch(request, title):
    annonces = Annonces.objects.filter(titre__contains=title).order_by('date')
    return render(request, 'annonces/list-annonces.html', locals())

# complete database with automatic values
def peupleur(request):
    ipsum = """Cupcake ipsum dolor sit amet wafer cookie. Bonbon topping candy canes croissant sweet sugar plum bear claw marshmallow. Jelly bear claw apple pie muffin sweet roll cookie marzipan. Powder candy canes jelly-o tiramisu cheesecake halvah cheesecake lollipop brownie. Pastry oat cake cookie. Chocolate cake bonbon sesame snaps chupa chups brownie cotton candy donut. Muffin cake cake carrot cake.
<br>
Apple pie fruitcake caramels powder muffin. Powder jelly soufflé. Sweet muffin chocolate bar cake pastry jujubes dessert gummies. Croissant dragée lemon drops dessert. Jelly beans caramels powder cake. Gummies icing apple pie cake lemon drops. Cupcake candy canes tootsie roll lollipop. Croissant dessert marshmallow icing jelly cheesecake pie."""

    users = len(User.objects.all()) - 1

    if(users < 1):
        user = User.objects.create_user('Soufian', 'aittirite.soufian@gmail.com', 'mypass')
        user1 = Annonceur(user=user,phone="06.01.02.03.04",site_web="http://atsn.me/")
        user1.save()
        user = User.objects.create_user('Pierre', 'pierre.truchot2@gmail.com', 'mypass2')
        user1 = Annonceur(user=user,phone="06.02.03.04.05",site_web="http://wesic.me/")
        user1.save()
        users = len(User.objects.all()) - 1
    
    for x in range(1,200):
        montant = 25 * x
        rangeid = random.randint(1,int(users))
        arg = str(rangeid)
        user = Annonceur.objects.get(user_id=arg)
        annonce = Annonces(titre="titre"+str(x),contenu=ipsum,montant=montant,annonceur=user)
        annonce.save()

    return HttpResponse("""
        <h1>Peuplement fait !</h1>
    """)

def inscription(request):
    #form = InscriptionForm(request.POST or None)
    # if (request.POST is not None):
    #     form = InscriptionForm(request.POST, instance=Annonces)
        
    #     if form.is_valid():
    #         annonce = form.save(commit=False)  # Ne sauvegarde pas directement l'annonce dans la base de données
    #         annonce.user_id = User.objects.all()[0]  # Nous ajoutons les attributs manquants
    #         annonce.save()
    #         envoi = True
    # else:
    form = InscriptionForm(instance=Annonces)
    
    # if form.is_valid(): 
    #     sujet = form.cleaned_data['sujet']
    #     message = form.cleaned_data['message']
    #     envoyeur = form.cleaned_data['envoyeur']
    #     renvoi = form.cleaned_data['renvoi']

    #     envoi = True
    
    return render(request, 'annonces/inscription.html', locals())