class Bola:
    def __init__(self, letra, numero):
        self.letra = letra
        self.numero = numero

    def visualizar_bola(self):
        return "{}{}".format(self.letra, self.numero)
