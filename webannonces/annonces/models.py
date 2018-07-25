from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Annonces(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de publication")
    montant = models.DecimalField(max_digits=19, decimal_places=5)
    annonceur = models.ForeignKey('Annonceur', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "annonces"
        ordering = ['date']

    def __str__(self):
        return self.titre

# class User(models.Model):
#     """docstring for User"""
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     email = models.CharField(max_length=100, unique=True)
#     phone = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)

#     class Meta:
#         verbose_name = "user"
#         ordering = ['firstname','lastname']

#     def __str__(self):
#         name = str(self.firstname)+" "+str(self.lastname)
#         return name

class Annonceur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    site_web = models.URLField(blank=True)
    phone = models.CharField(max_length=100)

    class Meta:
        verbose_name = "annonceur"

    def __str__(self):
        return "{0}".format(self.user.username)