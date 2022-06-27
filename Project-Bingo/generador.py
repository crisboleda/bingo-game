from bola import Bola
import random


class Generator:

    LETRAS = ("B", "I", "N", "G", "O")

    def generar_nueva_bola(self):
        letter = self.__generate_letter()
        number = self.__generate_number(letter)

        return Bola(letter, number)

    def __generate_letter(self):
        pos = random.randint(0, 4)
        return Generator.LETRAS[pos]

    def __generate_number(self, letter: str):

        number = 0

        if letter == "B":
            number = self.__generate_random_number(16, 30)

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
        return random.randint(start, end)

    def generate_all_ballot_numbers_by_letter(self, letter: str):
        ballot_numbers = []
        while len(ballot_numbers) < 15:
            ballot_number = self.__generate_number(letter)
            if not ballot_number in ballot_numbers:
                ballot_numbers.append(ballot_number)

        return ballot_numbers
