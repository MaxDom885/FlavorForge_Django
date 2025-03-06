from django.urls import path
from . import views

urlpatterns = [
    path('recette/<int:recette_id>/ajouter-favori/', views.ajouter_favori, name='ajouter_favori'),
    path('mes-favoris/', views.mes_favoris, name='mes_favoris'),
]