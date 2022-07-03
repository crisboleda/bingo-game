from unittest import TestCase
from generador import Generator
from ballot import Ballot


class GeneratorTest(TestCase):
    def setUp(self) -> None:
        self.generator = Generator()
        self.letter_b_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.letter_i_numbers = [
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
        ]
        self.letter_n_numbers = [
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
            44,
            45,
        ]
        self.letter_g_numbers = [
            46,
            47,
            48,
            49,
            50,
            51,
            52,
            53,
            54,
            55,
            56,
            57,
            58,
            59,
            60,
        ]
        self.letter_o_numbers = [
            61,
            62,
            63,
            64,
            65,
            66,
            67,
            68,
            69,
            70,
            71,
            72,
            73,
            74,
            75,
        ]

    def test_generate_a_new_ballot(self):
        ballot = self.generator.generar_nueva_bola()
        self.assertIsInstance(ballot, Ballot)

    def test_generate_ballot_letter_B(self):
        ballot_numbers = self.generator.generate_all_ballot_numbers_by_letter("B")
        is_correct_ballot_numbers_b = all(
            ballot_number in self.letter_b_numbers for ballot_number in ballot_numbers
        )

        self.assertEqual(len(ballot_numbers), 15)
        self.assertTrue(
            is_correct_ballot_numbers_b,
            "The number of a ballot does not correspond to the numbers of B",
        )

    def test_generate_ballot_letter_I(self):
        ballot_numbers = self.generator.generate_all_ballot_numbers_by_letter("I")
        is_correct_ballot_numbers_i = all(
            ballot_number in self.letter_i_numbers for ballot_number in ballot_numbers
        )

        self.assertEqual(len(ballot_numbers), 15)
        self.assertTrue(
            is_correct_ballot_numbers_i,
            "The number of a ballot does not correspond to the numbers of I",
        )

    def test_generate_ballot_letter_N(self):
        ballot_numbers = self.generator.generate_all_ballot_numbers_by_letter("N")
        is_correct_ballot_numbers_n = all(
            ballot_number in self.letter_n_numbers for ballot_number in ballot_numbers
        )

        self.assertEqual(len(ballot_numbers), 15)
        self.assertTrue(
            is_correct_ballot_numbers_n,
            "The number of a ballot does not correspond to the numbers of N",
        )

    def test_generate_ballot_letter_G(self):
        ballot_numbers = self.generator.generate_all_ballot_numbers_by_letter("G")
        is_correct_ballot_numbers_g = all(
            ballot_number in self.letter_g_numbers for ballot_number in ballot_numbers
        )

        self.assertEqual(len(ballot_numbers), 15)
        self.assertTrue(
            is_correct_ballot_numbers_g,
            "The number of a ballot does not correspond to the numbers of G",
        )

    def test_generate_ballot_letter_O(self):
        ballot_numbers = self.generator.generate_all_ballot_numbers_by_letter("O")
        is_correct_ballot_numbers_o = all(
            ballot_number in self.letter_o_numbers for ballot_number in ballot_numbers
        )

        self.assertEqual(len(ballot_numbers), 15)
        self.assertTrue(
            is_correct_ballot_numbers_o,
            "The number of a ballot does not correspond to the numbers of O",
        )
