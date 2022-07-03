from ballot import Ballot
from generador import Generator

class Logic:
    def __init__(self, generator: Generator, speaker):
        self.ballots = []
        self.generator = generator
        self.speaker = speaker

    def generate_ballot(self):
        while True:
            ballot = self.generator.generate_new_ballot()

            if self.buscar_bola(ballot):
                self.ballots.append(ballot)
                self.__say_ballot(ballot)
                return ballot

    def __say_ballot(self, ballot: Ballot):
        self.speaker.speak(ballot.show_ballot())

    def buscar_bola(self, ballot_generated: Ballot):
        for ballot in self.ballots:
            if ballot.number == ballot_generated.number:
                return False
        return True
