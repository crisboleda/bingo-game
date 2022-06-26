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

    def __generate_number(self, letra):

        numero = 0

        if letra == "B":
            numero = self.__generar_numero_random(1, 15)

        elif letra == "I":
            numero = self.__generar_numero_random(16, 30)

        elif letra == "N":
            numero = self.__generar_numero_random(31, 45)

        elif letra == "G":
            numero = self.__generar_numero_random(46, 60)

        elif letra == "O":
            numero = self.__generar_numero_random(61, 75)

        return numero

    def __generar_numero_random(self, inicio, fin):
        return random.randint(inicio, fin)

    def generate_all_ballot_numbers_by_letter(self, letter: str):
        ballot_numbers = []
        while len(ballot_numbers) < 15:
            ballot_number = self.__generate_number(letter)
            if not ballot_number in ballot_numbers:
                ballot_numbers.append(ballot_number)

        return ballot_numbers
