from django.urls import path
from . import views

urlpatterns = [
    path('recette/<int:recette_id>/commenter/', views.ajouter_commentaire, name='ajouter_commentaire'),
]