import win32com.client
from bola import Bola
from generador import Generador
from os import system


class Logic():

    def __init__(self, generador):
        self.bolas = []
        self.generador = generador
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")


    def generar_bola(self):
        system('cls')
        while True:
            bola = self.generador.generar_nueva_bola()
            
            if self.buscar_bola(bola):
                self.bolas.append(bola)
                self.__decir_bola(bola)
                return bola


    def __decir_bola(self, bola):
        self.speaker.Speak(bola.visualizar_bola())

    def buscar_bola(self, bola_generada):
        for bola in self.bolas:
            if bola.numero == bola_generada.numero:
                return False
        return True

