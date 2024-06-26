# Generated by Django 5.0.2 on 2024-04-03 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yugiohcard',
            name='card',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='yugiohdeck',
            name='deck',
        ),
        migrations.RemoveField(
            model_name='yugiohdeckcard',
            name='deck',
        ),
        migrations.RemoveField(
            model_name='yugiohdeckcard',
            name='card',
        ),
        migrations.RemoveField(
            model_name='yugiohformat',
            name='legal_cards',
        ),
        migrations.RemoveField(
            model_name='yugiohset',
            name='cards',
        ),
        migrations.DeleteModel(
            name='Binder',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='Deck',
        ),
        migrations.DeleteModel(
            name='YugiohDeck',
        ),
        migrations.DeleteModel(
            name='YugiohDeckCard',
        ),
        migrations.DeleteModel(
            name='YugiohFormat',
        ),
        migrations.DeleteModel(
            name='YugiohSet',
        ),
    ]
