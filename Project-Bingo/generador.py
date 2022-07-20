from ballot import Ballot
import random


class Generator:

    LETTERS = ("B", "I", "N", "G", "O")

    def generate_new_ballot(self) -> Ballot:
        """
        Generate a new ballot
        :return: Ballot, ballot generated
        """
        letter = self.__generate_letter()
        number = self.__generate_number(letter)

        return Ballot(letter, number)

    def __generate_letter(self):
        """
        Generate a letter
        :return: str, letter generated, Ie. "N"
        """
        position = random.randint(0, 4)
        return Generator.LETTERS[position]

    def __generate_number(self, letter: str):
        """
        Generate a number depending on letter
        :param letter: str, letter generated, Ie. "N"
        :return number: int, number generated, Ie. 36
        """

        number = 0

        if letter == "B":
            number = self.__generate_random_number(1, 15)

        elif letter == "I":
            number = self.__generate_random_number(16, 30)

        elif letter == "N":
            number = self.__generate_random_number(31, 45)

        elif letter == "G":
            number = self.__generate_random_number(46, 60)

        elif letter == "O":
            number = self.__generate_random_number(61, 75)

        return number

    def __generate_random_number(self, start: int, end: int):
        """
        Generate a random number between two numbers
        :param start: int, initial range, Ie. 31
        :param end: int, final range, Ie. 45
        :return: int, random number, Ie. 36
        """
        return random.randint(start, end)

    def generate_all_ballot_numbers_by_letter(self, letter: str):
        """
        Generate all ballot number by letter
        :param letter: str, letter to filter, Ie. "N"
        :return ballot_numbers: list, ballot numbers of a letter. Ie, [
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45
        ]
        """

        ballot_numbers = []
        while len(ballot_numbers) < 15:
            ballot_number = self.__generate_number(letter)
            if not ballot_number in ballot_numbers:
                ballot_numbers.append(ballot_number)

        return ballot_numbers
