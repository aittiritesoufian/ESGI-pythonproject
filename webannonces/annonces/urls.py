from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.home),
    path('annonce/<int:id_annonce>', views.getAnnonce),
    path('list/', views.list),
    path('list/<str:title>', views.listSearch),
    path('none/<str:string>', views.none, name="page_none"),
    path('peupleurbdd/', views.peupleur, name="peupleur"),
]