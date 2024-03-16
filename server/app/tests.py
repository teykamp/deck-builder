from django.test import TestCase
from app.models import Card, YugiohCard


class SingleCardTestCase(TestCase):
    CARD_ID_10000 = YugiohCard(card=Card(10000),
                               type='monster',
                               name='Gem-Knight Seraphinite',
                               englishAttribute='earth',
                               localizedAttribute='EARTH',
                               effectText='1 \"Gem-Knight\" monster + 1 LIGHT monster\nMust first be Fusion Summoned '
                                          'with the above Fusion Materials. During your Main Phase, you can Normal '
                                          'Summon/Set 1 monster in addition to your Normal Summon/Set. (You can only '
                                          'gain this effect once per turn.)',
                               level=5,
                               attack=2300,
                               defense=1400,
                               properties=['Fairy', 'Fusion', 'Effect'],
                               status=3)

    def setUp(self):
        test_card = Card.objects.create(id=10000)
        YugiohCard.objects.create(card=test_card,
                                  type='monster',
                                  name='Gem-Knight Seraphinite',
                                  englishAttribute='earth',
                                  localizedAttribute='EARTH',
                                  effectText='1 \"Gem-Knight\" monster + 1 LIGHT monster\nMust first be Fusion Summoned '
                                             'with the above Fusion Materials. During your Main Phase, you can Normal '
                                             'Summon/Set 1 monster in addition to your Normal Summon/Set. (You can only '
                                             'gain this effect once per turn.)',
                                  level=5,
                                  attack=2300,
                                  defense=1400,
                                  properties=['Fairy', 'Fusion', 'Effect'],
                                  status=3)

    def test_card_exists(self):
        card = YugiohCard.objects.get(card=Card(10000))
        self.assertEqual(self.CARD_ID_10000.effectText, card.effectText)
