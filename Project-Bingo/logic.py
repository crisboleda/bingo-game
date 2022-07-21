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

            if self.is_ballot_available(ballot):
                self.ballots.append(ballot)
                self.__say_ballot(ballot)
                return ballot

    def __say_ballot(self, ballot: Ballot):
        """
        Say the value of the ballot
        :param ballot: Ballot, ballot to say
        """
        self.speaker.speak(ballot.show_ballot())

    def is_ballot_available(self, ballot_generated: Ballot):
        """
        Valid if a ballot has not been generated
        :param ballot_generated: Ballot, ballot generated
        :return bool
        """
        for ballot in self.ballots:
            if ballot.number == ballot_generated.number:
                return False
        return True