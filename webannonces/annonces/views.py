from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime


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

def list(request, search):
    return HttpResponse("""
        <h1>Ceci sera une liste d'annonce</h1>
        <p>la liste affichera l'ensemble des annonces, ou seulement celles dont le titre/le contenu contien la chaîne suivante: {0}</p>
    """.format(search))

def none(request, string):
    return HttpResponse("""
        <h1>Ceci sera une page vierge</h1>
        <p>avec comme paramètre: {0}</p>
    """.format(string))

def addition(request, value):
    valeur = value*2
    return render(request, 'annonces/addition.html', locals())

def date_actuelle(request):
    return render(request, 'annonces/date.html', {'date': datetime.now()})