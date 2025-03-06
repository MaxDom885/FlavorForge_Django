from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Favori
from recettes.models import Recette
from django.shortcuts import render

@login_required
def ajouter_favori(request, recette_id):
    recette = get_object_or_404(Recette, id=recette_id)
    utilisateur = request.user

    # Vérifie si la recette est déjà dans les favoris
    favori, created = Favori.objects.get_or_create(
        utilisateur=utilisateur,
        recette=recette
    )

    # Si la recette est déjà dans les favoris, la supprimer
    if not created:
        favori.delete()

    return redirect('detail_recette', recette_id=recette.id)

@login_required
def mes_favoris(request):
    favoris = Favori.objects.filter(utilisateur=request.user)
    return render(request, 'favoris/mes_favoris.html', {'favoris': favoris})
