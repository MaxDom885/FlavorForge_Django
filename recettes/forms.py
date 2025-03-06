from django import forms
from .models import Recette

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['titre', 'description', 'ingredients', 'etapes', 'photo']