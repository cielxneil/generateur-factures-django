from django.contrib import admin
from .models import Facture, FactureProduit

class FactureProduitInline(admin.TabularInline):
    model = FactureProduit
    extra = 1

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    inlines = [FactureProduitInline]
    list_display = ("id", "date_creation")

@admin.register(FactureProduit)
class FactureProduitAdmin(admin.ModelAdmin):
    list_display = ("facture", "produit", "quantite")
