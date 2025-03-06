from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Utilisateur
from .forms import InscriptionForm, ProfilForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages


# Create your views here.

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            envoyer_email_verification(request, user)
            messages.success(request, "Inscription réussie ! Un e-mail de vérification a été envoyé à votre adresse e-mail.")
            return redirect('accueil')
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = InscriptionForm()
    return render(request, 'users/inscription.html', {'form': form})

@login_required
def profil(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre profil a été mis à jour avec succès.")
            return redirect('profil')  # Redirige vers la page de profil après la modification
    else:
        form = ProfilForm(instance=request.user)
    return render(request, 'users/profil.html', {'form': form})

def envoyer_email_verification(request, user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_url = request.build_absolute_uri(
        reverse('verifier_email', args=[uid, token])
    )
    subject = 'Vérifie ton email'
    message = render_to_string('users/email_verification.txt', {
        'user': user,
        'verification_url': verification_url,
    })
    send_mail(subject, message, 'maxdomyacoubou@gmail.com', [user.email])

def verifier_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Utilisateur.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Utilisateur.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_verified = True
        user.save()
        login(request, user)
        return redirect('profil')
    else:
        return render(request, 'users/email_verification_invalide.html')