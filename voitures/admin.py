from django.contrib import admin
from .models import Voiture, Categorie

@admin.register(Voiture)
class VoitureAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie','marque', 'proprietaire', 'valide')
    list_filter = ('valide', 'categorie')
    actions = ['valider_voitures']

    def valider_voitures(self, request, queryset):
        queryset.update(valide=True)
    valider_voitures.short_description = "Valider les voitures sélectionnées"

admin.site.register(Categorie)
