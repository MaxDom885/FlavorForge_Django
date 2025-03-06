from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('publier/', views.publier_recette, name='publier_recette'),
    path('recette/<int:recette_id>/', views.detail_recette, name='detail_recette'),
]