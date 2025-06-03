from django.shortcuts import render, redirect, get_object_or_404
from .models import Voiture, Categorie
from .forms import VoitureForm 
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

@login_required
def liste_voitures(request):
    if request.user.is_staff:
        voitures = Voiture.objects.all()
    else:
        voitures = Voiture.objects.filter(valide=True) | Voiture.objects.filter(proprietaire=request.user)
    return render(request, 'voitures/liste.html', {'voitures': voitures})

@login_required
def ajouter_voiture(request):
    if request.user.is_staff:

        return redirect('liste_voitures')

    if request.method == 'POST':
        form = VoitureForm(request.POST)
        if form.is_valid():
            voiture = form.save(commit=False)
            voiture.proprietaire = request.user
            voiture.valide = False
            voiture.save()
            return redirect('liste_voitures')
    else:
        form = VoitureForm()
    return render(request, 'voitures/form.html', {'form': form})

@login_required
def modifier_voiture(request, pk):
    voiture = get_object_or_404(Voiture, pk=pk, proprietaire=request.user)
    if request.method == 'POST':
        form = VoitureForm(request.POST, instance=voiture)
        if form.is_valid():
            form.save()
            return redirect('liste_voitures')
    else:
        form = VoitureForm(instance=voiture)
    return render(request, 'voitures/form.html', {'form': form})

@login_required
def supprimer_voiture(request, pk):
    voiture = get_object_or_404(Voiture, pk=pk, proprietaire=request.user)
    if request.method == 'POST':
        voiture.delete()
        return redirect('liste_voitures')
    return render(request, 'voitures/supprimer_voiture.html', {'voiture': voiture})

@login_required
def mes_voitures(request):
    voitures = Voiture.objects.filter(proprietaire=request.user)
    return render(request, 'voitures/mes_voitures.html', {'voitures': voitures})

@staff_member_required
def valider_voitures(request):
    voitures = Voiture.objects.filter(valide=False)
    return render(request, 'voitures/valider_voitures.html', {'voitures': voitures})

@staff_member_required
def accepter_voiture(request, pk):
    voiture = get_object_or_404(Voiture, pk=pk)
    voiture.valide = True
    voiture.save()
    return redirect('valider_voitures')




