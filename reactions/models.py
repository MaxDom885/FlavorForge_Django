from django.db import models
from django.contrib.auth import get_user_model
from recettes.models import Recette

Utilisateur = get_user_model()

class Reaction(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    REACTION_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]

    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name='reactions')
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=REACTION_CHOICES)
    date_publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recette', 'utilisateur')  # Un utilisateur ne peut réagir qu'une fois par recette

    def __str__(self):
        return f"{self.utilisateur.username} a réagi avec un {self.type} sur {self.recette.titre}"