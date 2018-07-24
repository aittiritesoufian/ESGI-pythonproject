from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.home),
    path('annonce/<int:id_annonce>', views.getAnnonce),
    path('list/<str:search>', views.list),
    path('none/<str:string>', views.none, name="page_none"),
    path('addition/<int:value>', views.addition, name="addition"),
    path('date/', views.date_actuelle, name="date"),
]