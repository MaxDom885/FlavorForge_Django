"""
URL configuration for flavorforge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from flavorforge import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),  # Point d'entrée
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('commentaires/', include('commentaires.urls')),
    path('recettes/', include('recettes.urls')),
    path('reactions/', include('reactions.urls')),
    path('favoris/', include('favoris.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
