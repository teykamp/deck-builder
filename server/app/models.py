from django.conf import settings
from django.db import models

class Card(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    englishAttribute = models.CharField(max_length=32)
    localizedAttribute = models.CharField(max_length=32)
    effectText = models.CharField(max_length=512)
    level = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    properties = models.JSONField() # JSON list of strings containing the properties
    status = models.IntegerField()


#class Deck(models.Model):
#    name = models.CharField(max_length=100)
#    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    date_created = models.DateTimeField()
#
#
## Collection of cards in unorganized format; might contain cards from different TCGs
#class Binder(models.Model):
#    name = models.CharField(max_length=100)
#    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    cards = models.ManyToManyField(Card)
#
#
#class YugiohCard(models.Model):
#    card = models.OneToOneField(Card, on_delete=models.CASCADE)
#    name = models.CharField(max_length=100)
#    artist = models.CharField(max_length=50)
#    foil = models.BooleanField()
#
#
#class YugiohDeck(models.Model):
#    deck = models.OneToOneField(Deck, on_delete=models.CASCADE)
#    cards = models.ManyToManyField(Card, through="YugiohDeckCard")
#
#
#class YugiohDeckCard(models.Model):
#    class Type(models.TextChoices):
#        MAIN = "M"
#        EXTRA = "E"
#        SIDE = "S"
#
#    deck = models.ForeignKey(YugiohDeck, on_delete=models.CASCADE)
#    card = models.ForeignKey(YugiohCard, on_delete=models.CASCADE)
#
#
#class YugiohFormat(models.Model):
#    name = models.CharField(max_length=50)
#    legal_cards = models.ManyToManyField(YugiohCard)
#
#
#class YugiohSet(models.Model):
#    name = models.CharField(max_length=50)
#    cards = models.ManyToManyField(YugiohCard)
#    date_released = models.DateTimeField()
