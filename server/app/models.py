from django.conf import settings
from django.db import models


class Card(models.Model):
    pass


class Deck(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField()


# Collection of cards in unorganized format; might contain cards from different TCGs
class Binder(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card)


class YugiohCard(models.Model):
    card = models.OneToOneField(Card, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    foil = models.BooleanField()


class YugiohDeck(models.Model):
    deck = models.OneToOneField(Deck, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card, through="YugiohDeckCard")


class YugiohDeckCard(models.Model):
    class Type(models.TextChoices):
        MAIN = "M"
        EXTRA = "E"
        SIDE = "S"

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)


class YugiohFormat(models.Model):
    name = models.CharField(max_length=50)
    legal_cards = models.ManyToManyField(YugiohCard)


class YugiohSet(models.Model):
    name = models.CharField(max_length=50)
    cards = models.ManyToManyField(YugiohCard)
    date_released = models.DateTimeField()
