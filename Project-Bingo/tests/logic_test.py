from importlib.resources import path
from unittest import TestCase
from unittest.mock import Mock, patch

from generador import Generator
from speaker.gtts_speaker import GTTSpeaker
from bola import Bola
from logic import Logic


class LogicTest(TestCase):
    def setUp(self) -> None:
        self.generator = Generator()
        self.speaker = GTTSpeaker("es")
        self.logic = Logic(self.generator, self.speaker)

    @patch.object(GTTSpeaker, "speak", return_value=None)
    def test_generate_ballots(self, gtt_speak_mock: Mock) -> None:
        ballot = self.logic.generar_bola()

        self.assertEqual(len(self.logic.bolas), 1)
        self.assertIsInstance(ballot, Bola)
        gtt_speak_mock.assert_called_once_with(ballot.visualizar_bola())

    def test_validate_ballot_generated(self) -> None:
        old_ballot = Bola("B", 11)
        self.logic.bolas = [old_ballot]

        new_ballot_b = Bola("B", 11)
        new_ballot_g = Bola("G", 47)

        self.assertFalse(self.logic.buscar_bola(new_ballot_b))
        self.assertTrue(self.logic.buscar_bola(new_ballot_g))
