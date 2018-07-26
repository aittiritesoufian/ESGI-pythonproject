from django import forms
from .models import Annonces, Annonceur
from django.contrib.auth.models import User

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonces
        fields = ('titre','contenu','date','montant',)

class InscriptionForm(forms.Form):
	username = forms.CharField(max_length=100,label="Votre nom d'utilisateur*")
	first_name = forms.CharField(max_length=100,label="Votre Prénom*")
	last_name = forms.CharField(max_length=100,label="Votre Nom*")
	email = forms.EmailField(max_length=100,label="Votre adresse mail*")
	password = forms.CharField(widget=forms.PasswordInput)
	phone = forms.CharField(max_length=100,label="Votre numéro de téléphone")
	site_web = forms.URLField()


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)