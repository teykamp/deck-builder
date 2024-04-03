from django.test import TestCase
from .models import YugiohCard


class SingleCardTestCase(TestCase):
    def setUp(self):
        self.CARD_ID_7938 = YugiohCard.objects.create(
                pk=7938,
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
        try:
            card = YugiohCard.objects.get(pk=7938)
        except YugiohCard.DoesNotExist:
            card = None

        self.assertTrue(card)
        self.assertEqual(self.CARD_ID_7938.name, card.name)
