from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('connexion/', auth_views.LoginView.as_view(template_name='users/connexion.html'), name='connexion'),
    path('deconnexion/', auth_views.LogoutView.as_view(next_page='/'), name='deconnexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('profil/', views.profil, name='profil'),
    path('verifier-email/<uidb64>/<token>/', views.verifier_email, name='verifier_email'),
    path('reinitialiser-mot-de-passe/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('reinitialiser-mot-de-passe/envoye/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reinitialiser/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reinitialiser-mot-de-passe/complet/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

]