from unittest import TestCase
from bola import Bola


class BallTest(TestCase):
    def setUp(self) -> None:
        self.ballot_one = Bola("B", 12)
        self.ballot_two = Bola("I", 20)
        self.ballot_three = Bola("n", 30)

    def test_show_ball(self):
        self.assertEqual("B12", self.ballot_one.visualizar_bola())
        self.assertEqual("I20", self.ballot_two.visualizar_bola())
        self.assertEqual("N30", self.ballot_three.visualizar_bola())
