from unittest import TestCase
from unittest.mock import MagicMock, Mock, call, patch
import pygame

from game import Game


class GameTest(TestCase):
    def setUp(self):
        logic = Mock(None)
        api = Mock(None)
        self.game = Game(logic=logic, api=api, seconds_delay=5, mode="test")

    @patch.object(Game, "generate_ball_worker", return_value=None)
    def test_event_mouse_pause_game(self, generate_ball_worker_mock: MagicMock):
        with patch("game.pygame") as pygame_mock:
            pygame_mock.MOUSEBUTTONUP = pygame.MOUSEBUTTONUP
            pygame_mock.event.get.return_value = [MagicMock(type=pygame.MOUSEBUTTONUP)]
            pygame_mock.mouse.get_pos.return_value = (100, 200)
            self.game.start_game()

            self.assertFalse(self.game.is_pause)
