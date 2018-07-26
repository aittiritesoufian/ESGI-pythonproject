from django import forms
from .models import Annonces, Annonceur
from django.contrib.auth.models import User

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonces
        fields = ('titre','contenu','date','montant',)

class InscriptionForm(forms.Form):
    # class Meta:
    #     model = User
    #     fields = ('username','first_name','last_name','email','password')
	username = forms.CharField(max_length=100,label="Votre nom d'utilisateur*")
	first_name = forms.CharField(max_length=100,label="Votre Prénom*")
	last_name = forms.CharField(max_length=100,label="Votre Nom*")
	email = forms.EmailField(max_length=100,label="Votre adresse mail*")
	password = forms.PasswordInput(render_value=False)
	phone = forms.CharField(max_length=100,label="Votre numéro de téléphone")
	site_web = forms.URLInput(label="Votre site internet")

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)