from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur
from django.utils.translation import gettext_lazy as _

class InscriptionForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Adresse e-mail",
        help_text="Nous enverrons un e-mail de confirmation à cette adresse."
    )
    photo_profil = forms.ImageField(
        required=False,
        label="Photo de profil",
        help_text="Téléchargez une photo pour personnaliser votre profil."
    )

    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'password1', 'password2', 'photo_profil']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personnaliser les labels et les messages d'aide
        self.fields['username'].label = "Nom d'utilisateur"
        self.fields['username'].help_text = (
            "150 caractères maximum. Lettres, chiffres et @/./+/-/_ uniquement."
        )
        self.fields['password1'].label = "Mot de passe"
        self.fields['password1'].help_text = (
            "Votre mot de passe doit contenir au moins 8 caractères, "
            "ne pas être trop courant et ne pas être entièrement numérique."
        )
        self.fields['password2'].label = "Confirmation du mot de passe"
        self.fields['password2'].help_text = "Entrez le même mot de passe que ci-dessus pour vérification."

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'photo_profil']
        photo_profil = forms.ImageField(required=False, label="Photo de profil")


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Utilisateur.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("Cet e-mail est déjà utilisé.")
        return email
