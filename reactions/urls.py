from django.urls import path
from . import views

urlpatterns = [
    path('recette/<int:recette_id>/reaction/<str:reaction_type>/', views.ajouter_reaction, name='ajouter_reaction'),
]