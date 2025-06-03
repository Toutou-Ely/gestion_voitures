from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_voitures, name='liste_voitures'),
    path('ajouter/', views.ajouter_voiture, name='ajouter_voiture'),
    path('modifier/<int:pk>/', views.modifier_voiture, name='modifier_voiture'),
    path('supprimer/<int:pk>/', views.supprimer_voiture, name='supprimer_voiture'),
    path('mes/', views.mes_voitures, name='mes_voitures'),
    path('valider/', views.valider_voitures, name='valider_voitures'),
    path('accepter/<int:pk>/', views.accepter_voiture, name='accepter_voiture'),
]
