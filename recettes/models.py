from django.db import models
from django.contrib.auth import get_user_model

Utilisateur = get_user_model()

class Recette(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    etapes = models.TextField()
    photo = models.ImageField(upload_to='recettes/', blank=True, null=True)
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
    
class Commentaire(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name='recettes_commentaires')
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='recettes_commentaires')
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire par {self.auteur} sur {self.recette.titre}"