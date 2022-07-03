class Ballot:
    def __init__(self, letter: str, number: int):
        self.letter = letter
        self.number = number

    def show_ballot(self):
        return "{}{}".format(self.letter.upper(), self.number)
