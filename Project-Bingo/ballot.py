class Ballot:
    def __init__(self, letra: str, numero: int):
        self.letra = letra
        self.numero = numero

    def visualizar_bola(self):
        return "{}{}".format(self.letra.upper(), self.numero)
