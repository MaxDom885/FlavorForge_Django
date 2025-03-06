from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Utilisateur(AbstractUser):
    photo_profil = models.ImageField(upload_to='profiles/', blank=True, null=True)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Profil(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Profil de {self.user.username}"

    def __str__(self):
        return f"Profil de {self.user.username}"