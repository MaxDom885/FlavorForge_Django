from django.db import models
from django.contrib.auth import get_user_model
from recettes.models import Recette

Utilisateur = get_user_model()

class Commentaire(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire par {self.auteur} sur {self.recette.titre}"