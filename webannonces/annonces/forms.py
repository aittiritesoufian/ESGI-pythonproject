from django import forms
from .models import Annonces

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Annonces
        fields = '__all__'