from django.test import TestCase
from app.models import Card

class SingleCardTestCase(TestCase):
    def setUp(self):
        Card.objects.create(id=10000,
                            type='monster',
                            name='Gem-Knight Seraphinite',
                            englishAttribute='earth',
                            localizedAttribute='EARTH',
                            effectText='1 \"Gem-Knight\" monster + 1 LIGHT monster\nMust first be Fusion Summoned with the above Fusion Materials. During your Main Phase, you can Normal Summon/Set 1 monster in addition to your Normal Summon/Set. (You can only gain this effect once per turn.)',
                            level=5,
                            attack=2300,
                            defense=1400,
                            properties=['Fairy', 'Fusion', 'Effect'],
                            status='Unlimited')

    def test_card_exists(self):
        card = Card.objects.get(id=10000)
        self.assertTrue(card.name == 'Gem-Knight Seraphinite')
