from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecetteForm
from .models import Recette
from django.shortcuts import get_object_or_404


def accueil(request):
    recettes = Recette.objects.all().order_by('-date_publication')
    return render(request, 'recettes/accueil.html', {'recettes': recettes})

@login_required
def publier_recette(request):
    if request.method == 'POST':
        form = RecetteForm(request.POST, request.FILES)
        if form.is_valid():
            recette = form.save(commit=False)
            recette.auteur = request.user
            recette.save()
            return redirect('accueil')
    else:
        form = RecetteForm()
    return render(request, 'recettes/publier_recette.html', {'form': form})

def detail_recette(request, recette_id):
    recette = get_object_or_404(Recette, id=recette_id)
    ingredients_list = recette.ingredients.split(',')
    etapes_list = recette.etapes.split('.')
    likes_count = recette.reactions.filter(type='like').count()
    dislikes_count = recette.reactions.filter(type='dislike').count()

    return render(request, 'recettes/detail_recette.html', {
        'recette': recette,
        'ingredients_list': ingredients_list,
        'etapes_list': etapes_list,
        'likes_count': likes_count,
        'dislikes_count': dislikes_count,
    })

