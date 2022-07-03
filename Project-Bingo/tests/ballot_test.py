from unittest import TestCase
from ballot import Ballot


class BallotTest(TestCase):
    def setUp(self) -> None:
        self.ballot_one = Ballot("B", 12)
        self.ballot_two = Ballot("I", 20)
        self.ballot_three = Ballot("n", 30)

    def test_show_ballot(self):
        self.assertEqual("B12", self.ballot_one.show_ballot())
        self.assertEqual("I20", self.ballot_two.show_ballot())
        self.assertEqual("N30", self.ballot_three.show_ballot())
