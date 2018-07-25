from django import forms
from .models import Annonces

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonces
        exclude = ('annonceur')

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)