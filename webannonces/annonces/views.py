from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from annonces.models import User, Annonces
import random
import pickle


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur les annonces !</h1>
        <p>Les annonces c'est trop génial !</p>
    """)

def getAnnonce(request, id_annonce):
    if id_annonce > 300:
        return redirect('page_none', string="this is a string")
    if id_annonce > 200:
        return redirect(home)
    if id_annonce > 100:
        raise Http404
    return HttpResponse("""
        <h1>Ceci sera une annonce</h1>
        <p>l'annonce récupérer aura pour id: {0} </p>
    """.format(id_annonce))

def list(request):
    annonces = Annonces.objects.all().order_by('date')
    return render(request, 'annonces/list-annonces.html', locals())

def listSearch(request, title):
    annonces = Annonces.objects.filter(titre__contains=title).order_by('date')
    return render(request, 'annonces/list-annonces.html', locals())

def none(request, string):
    return HttpResponse("""
        <h1>Ceci sera une page vierge</h1>
        <p>avec comme paramètre: {0}</p>
    """.format(string))

# complete database with automatic values
def peupleur(request):
    ipsum = """Cupcake ipsum dolor sit amet wafer cookie. Bonbon topping candy canes croissant sweet sugar plum bear claw marshmallow. Jelly bear claw apple pie muffin sweet roll cookie marzipan. Powder candy canes jelly-o tiramisu cheesecake halvah cheesecake lollipop brownie. Pastry oat cake cookie. Chocolate cake bonbon sesame snaps chupa chups brownie cotton candy donut. Muffin cake cake carrot cake.

Apple pie fruitcake caramels powder muffin. Powder jelly soufflé. Sweet muffin chocolate bar cake pastry jujubes dessert gummies. Croissant dragée lemon drops dessert. Jelly beans caramels powder cake. Gummies icing apple pie cake lemon drops. Cupcake candy canes tootsie roll lollipop. Croissant dessert marshmallow icing jelly cheesecake pie."""

    users = len(User.objects.all()) - 1

    if(users < 1):
        user1 = User(firstname="Soufian",lastname="AIT TIRITE",email="aittirite.soufian@gmail.com",phone="06.01.02.03.04",password="mypass")
        user1.save()
        user1 = User(firstname="Pierre",lastname="TRUCHOT",email="pierre.truchot2@gmail.com",phone="06.02.03.04.05",password="mypass2")
        user1.save()
        users = len(User.objects.all()) - 1
    
    for x in range(1,200):
        montant = 25 * x
        rangeid = random.randint(1,int(users))
        arg = str(rangeid)
        user = User.objects.get(id=arg)
        annonce = Annonces(titre="titre"+str(x),contenu=ipsum,montant=montant,user_id=user)
        annonce.save()

    return HttpResponse("""
        <h1>Peuplement fait !</h1>
    """)