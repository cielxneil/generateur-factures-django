from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def page_accueil(request):
    return HttpResponse("Bienvenue sur la page d'accueil !") 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page_accueil, name='accueil'),
    path('produits/', include('produits.urls')),
    path('factures/', include('factures.urls')),
]
