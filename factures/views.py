from django.shortcuts import render, get_object_or_404, redirect
from .models import Facture
from .forms import FactureForm

def liste_factures(request):
    factures = Facture.objects.all()
    return render(request, 'factures/facture_list.html', {'page_obj': factures})

def detail_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    return render(request, 'factures/facture_detail.html', {'facture': facture})

def modifier_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        form = FactureForm(request.POST, instance=facture)
        if form.is_valid():
            form.save()
            return redirect('factures:liste')
    else:
        form = FactureForm(instance=facture)
    return render(request, 'factures/facture_form.html', {'form': form})

def supprimer_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        facture.delete()
        return redirect('factures:liste')
    return render(request, 'factures/facture_confirm_delete.html', {'facture': facture})

def creer_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('factures:liste')
    else:
        form = FactureForm()
    return render(request, 'factures/facture_form.html', {'form': form})
