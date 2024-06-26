# Generated by Django 5.0.2 on 2024-04-03 17:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('app', '0001_initial'), ('app', '0002_remove_yugiohcard_card_remove_deck_owner_and_more')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='YugiohCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=64)),
                ('englishAttribute', models.CharField(max_length=32)),
                ('localizedAttribute', models.CharField(max_length=32)),
                ('effectText', models.CharField(max_length=512)),
                ('level', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('properties', models.JSONField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]
