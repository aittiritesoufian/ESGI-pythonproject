from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur les annonces !</h1>
        <p>Les annonces c'est trop génial !</p>
    """)

def getAnnonce(request, id_annonce):
	return HttpResponse("""
        <h1>Ceci sera une annonce</h1>
        <p>l'annonce récupérer aura pour id: {0} </p>
    """.format(id_annonce))

def list(request, search):
	return HttpResponse("""
        <h1>Ceci sera une liste d'annonce</h1>
        <p>la liste affichera l'ensemble des annonces, ou seulement celles dont le titre/le contenu contien la chaîne suivante: {0}</p>
    """.format(search))