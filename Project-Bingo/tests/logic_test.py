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
