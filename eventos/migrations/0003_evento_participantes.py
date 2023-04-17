# Generated by Django 4.2 on 2023-04-15 02:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0002_evento_criador'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='participantes',
            field=models.ManyToManyField(blank=True, null=True, related_name='evento_participante', to=settings.AUTH_USER_MODEL),
        ),
    ]
