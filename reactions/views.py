from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reaction
from recettes.models import Recette

@login_required
def ajouter_reaction(request, recette_id, reaction_type):
    recette = get_object_or_404(Recette, id=recette_id)
    utilisateur = request.user

    # Vérifie si l'utilisateur a déjà réagi à cette recette
    reaction, created = Reaction.objects.get_or_create(
        recette=recette,
        utilisateur=utilisateur,
        defaults={'type': reaction_type}
    )

    # Si l'utilisateur a déjà réagi, met à jour la réaction
    if not created:
        if reaction.type == reaction_type:
            reaction.delete()  # Annule la réaction si l'utilisateur clique à nouveau sur le même bouton
        else:
            reaction.type = reaction_type
            reaction.save()

    return redirect('detail_recette', recette_id=recette.id)