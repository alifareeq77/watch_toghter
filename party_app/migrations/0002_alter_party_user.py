# Generated by Django 4.2.2 on 2024-02-05 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('party_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='party_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
