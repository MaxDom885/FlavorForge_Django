from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CommentaireForm
from recettes.models import Recette

@login_required
def ajouter_commentaire(request, recette_id):
    recette = get_object_or_404(Recette, id=recette_id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.recette = recette
            commentaire.auteur = request.user
            commentaire.save()
            return redirect('detail_recette', recette_id=recette.id)
    else:
        form = CommentaireForm()
    return render(request, 'commentaires/ajouter_commentaire.html', {'form': form, 'recette': recette})