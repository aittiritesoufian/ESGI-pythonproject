from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.contrib.auth.models import User
from annonces.models import Annonceur, Annonces
from .forms import AnnonceForm, ConnexionForm, InscriptionForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import random
import pickle


def home(request):
    return render(request, 'annonces/home.html')

def getAnnonce(request, id_annonce):
    annonce = Annonces.objects.get(id=id_annonce)

    if(annonce is None):
        return redirect('home')
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

    users = len(User.objects.all())

    if(users < 1):
        user = User.objects.create_user('Soufian', 'aittirite.soufian@gmail.com', 'mypass')
        user1 = Annonceur(user=user,phone="06.01.02.03.04",site_web="http://atsn.me/")
        user1.save()
        user = User.objects.create_user('Pierre', 'pierre.truchot2@gmail.com', 'mypass2')
        user1 = Annonceur(user=user,phone="06.02.03.04.05",site_web="http://wesic.me/")
        user1.save()
        users = len(User.objects.all())
    
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
    form = InscriptionForm(request.POST or None)
    
    if form.is_valid():
        user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        annonceur = Annonceur(user=user)
        annonceur.save()
        envoi = True
        return redirect('connexion')
    
    return render(request, 'annonces/inscription.html', locals())

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect('mes_annonces')
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'annonces/login.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

@login_required(redirect_field_name='connexion')
def mesAnnonces(request):
    annonceur = Annonceur.objects.get(user=request.user)
    annonces = Annonces.objects.filter(annonceur=annonceur)
    return render(request, 'annonces/mes-annonces.html', locals())

@login_required(redirect_field_name='connexion')
def editAnnonce(request, id_annonce):
    # annonce = Annonces.objects.get(id=id_annonce)
    annonce = get_object_or_404(Annonces, id=id_annonce)
    form = AnnonceForm(request.POST, instance=annonce)
    if form.is_valid():
        annonce = form.save(commit=False)  # Ne sauvegarde pas directement l'annonce dans la base de données
        annonce.annonceur = Annonceur.objects.get(user=request.user)  # Nous ajoutons les attributs manquants
        annonce.save()
        envoi = True
    return render(request, 'annonces/edit-annonces.html', locals())