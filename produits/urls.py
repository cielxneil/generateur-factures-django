from django.urls import path
from . import views

app_name = 'produits'

urlpatterns = [
    path('', views.liste_produits, name='liste'),              # Liste des produits
    path('ajouter/', views.ajouter_produit, name='ajouter'),   # Ajouter un produit
    path('<int:pk>/modifier/', views.modifier_produit, name='modifier'),  # Modifier un produit par PK
    path('<int:pk>/supprimer/', views.supprimer_produit, name='supprimer'),  # Supprimer un produit par PK
]
