from django.urls import path
from . import views

app_name = 'factures'

urlpatterns = [
    path('', views.liste_factures, name='liste'),                 # Liste toutes les factures
    path('<int:pk>/', views.detail_facture, name='detail'),       # Détail d’une facture
    path('<int:pk>/edit/', views.modifier_facture, name='edit'),  # Modifier une facture
    path('<int:pk>/delete/', views.supprimer_facture, name='delete'),  # Supprimer une facture
    path('create/', views.creer_facture, name='create'),          # Créer une facture   # Po
]
