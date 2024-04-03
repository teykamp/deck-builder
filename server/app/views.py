from django.http import HttpResponse
from django.shortcuts import render
from .models import YugiohCard
import json

def index(request):
    return HttpResponse('hello world. yippee!')

def testcard(request):
    return HttpResponse(json.dumps({
            'id': 7938,
            'type': 'monster',
            'image': 'https://static.wikia.nocookie.net/yugioh/images/2/2a/GemKnightSeraphinite-SHVA-EN-ScR-1E.png',
            'name': 'Gem-Knight Seraphinite',
            'englishAttribute':'earth',
            'localizedAttribute':'EARTH',
            'effectText':'1 \"Gem-Knight\" monster + 1 LIGHT monster\nMust first be Fusion Summoned with the above Fusion Materials. During your Main Phase, you can Normal Summon/Set 1 monster in addition to your Normal Summon/Set. (You can only gain this effect once per turn.)',
            'level':5,
            'attack':2300,
            'defense':1400,
            'properties':['Fairy', 'Fusion', 'Effect'],
            'status':3}),
            content_type='application/json')

def yugiohcard(request, card_id):
    card = YugiohCard.objects.get(pk=card_id)
    return HttpResponse(json.dumps({
            'id': card.id,
            'type': card.type,
            'image': 'https://static.wikia.nocookie.net/yugioh/images/2/2a/GemKnightSeraphinite-SHVA-EN-ScR-1E.png',
            'name': card.name,
            'englishAttribute': card.englishAttribute,
            'localizedAttribute': card.localizedAttribute,
            'effectText': card.effectText,
            'level': card.level,
            'attack': card.attack,
            'defense': card.defense,
            'properties': card.properties,
            'status': card.status}),
            content_type='application/json')
