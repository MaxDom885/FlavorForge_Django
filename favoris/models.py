from django.db import models
from django.contrib.auth import get_user_model
from recettes.models import Recette

Utilisateur = get_user_model()

class Favori(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('utilisateur', 'recette')  # Un utilisateur ne peut ajouter une recette qu'une seule fois aux favoris

    def __str__(self):
        return f"{self.utilisateur.username} a ajouté {self.recette.titre} aux favoris"