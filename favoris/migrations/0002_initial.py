# Generated by Django 5.0.6 on 2025-03-03 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('favoris', '0001_initial'),
        ('recettes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favori',
            name='recette',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recettes.recette'),
        ),
    ]
