from django.contrib import admin
from .models import Produit

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ("nom", "prix", "date_peremption")
    search_fields = ("nom",)
