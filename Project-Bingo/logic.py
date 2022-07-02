class Logic:
    def __init__(self, generator, speaker):
        self.bolas = []
        self.generator = generator
        self.speaker = speaker

    def generar_bola(self):
        while True:
            bola = self.generator.generar_nueva_bola()

            if self.buscar_bola(bola):
                self.bolas.append(bola)
                self.__decir_bola(bola)
                return bola

    def __decir_bola(self, bola):
        self.speaker.speak(bola.visualizar_bola())

    def buscar_bola(self, bola_generada):
        for bola in self.bolas:
            if bola.numero == bola_generada.numero:
                return False
        return True
