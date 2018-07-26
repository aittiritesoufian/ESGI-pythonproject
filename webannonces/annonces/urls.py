from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('annonce/<int:id_annonce>', views.getAnnonce, name="single_annonce"),
    path('list/', views.list, name="liste_annonces"),
    path('list/<str:title>', views.listSearch),
    path('peupleurbdd/', views.peupleur, name="peupleur"),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('mes-annonces/', views.mesAnnonces, name='mes_annonces'),
    path('mes-annonces/<int:id_annonce>', views.editAnnonce, name='edit_annonces'),
    path('ajout-annonces/', views.addAnnonce, name='new_annonce'),
]
