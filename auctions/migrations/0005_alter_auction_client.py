# Generated by Django 4.1.4 on 2023-01-10 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auction_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client', to=settings.AUTH_USER_MODEL),
        ),
    ]
