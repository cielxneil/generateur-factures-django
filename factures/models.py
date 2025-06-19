from django.db import models
from produits.models import Produit

class Facture(models.Model):
    client = models.CharField(max_length=100)  # Ajout du champ manquant
    date_creation = models.DateTimeField(auto_now_add=True)

    def total(self):
        return sum([item.sous_total() for item in self.produits.all()])

    def __str__(self):
        return f"Facture #{self.id} - {self.date_creation.date()}"

class FactureProduit(models.Model):
    facture = models.ForeignKey(Facture, related_name='produits', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def sous_total(self):
        return self.produit.prix * self.quantite

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"
