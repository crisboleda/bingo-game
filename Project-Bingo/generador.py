from bola import Bola
import random


class Generador:

    LETRAS = ("B", "I", "N", "G", "O")

    def generar_nueva_bola(self):
        letra = self.__generar_letra()
        numero = self.__generar_numero(letra)

        return Bola(letra, numero)

    def __generar_letra(self):
        pos = random.randint(0, 4)
        return Generador.LETRAS[pos]

    def __generar_numero(self, letra):

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
