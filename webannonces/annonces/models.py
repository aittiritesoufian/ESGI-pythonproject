from django.db import models
from django.utils import timezone

class Annonces(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de publication")
    montant = models.DecimalField(max_digits=19, decimal_places=5)
    
    class Meta:
        verbose_name = "annonces"
        ordering = ['date']
    
    def __str__(self):
        return self.titre