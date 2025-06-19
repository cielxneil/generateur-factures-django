from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit
from .forms import ProduitForm
from django.core.paginator import Paginator

def liste_produits(request):
    """Affiche la liste des produits avec pagination."""
    produits = Produit.objects.all().order_by('nom')
    paginator = Paginator(produits, 5)  # 5 produits par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'produits/produit_list.html', {'page_obj': page_obj})

def ajouter_produit(request):
    """Ajoute un produit."""
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produits:liste')
    else:
        form = ProduitForm()
    return render(request, 'produits/produit_form.html', {'form': form})

def modifier_produit(request, pk):
    """Modifie un produit existant."""
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produits:liste')
    else:
        form = ProduitForm(instance=produit)

    return render(request, 'produits/produit_form.html', {'form': form})

def supprimer_produit(request, pk):
    """Supprime un produit."""
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('produits:liste')
    return render(request, 'produits/produit_confirm_delete.html', {'produit': produit})
