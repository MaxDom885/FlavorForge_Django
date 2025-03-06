from django.db.models.signals import post_save
from django.dispatch import receiver
from flavorforge.users.models import Utilisateur,Profil

@receiver(post_save, sender=Utilisateur)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)

@receiver(post_save, sender=Utilisateur)
def save_user_profile(sender, instance, **kwargs):
    instance.profil.save()