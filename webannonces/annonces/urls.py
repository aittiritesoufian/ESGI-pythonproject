from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.home),
    path('annonce/<int:id_annonce>', views.getAnnonce),
    path('list/<str:search>', views.list),
]