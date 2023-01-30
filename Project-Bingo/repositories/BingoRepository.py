from abc import ABC, abstractmethod
from ballot import Ballot


class BingoRepository(ABC):
    @abstractmethod
    def create_game(self):
        pass

    @abstractmethod
    def end_game(self):
        pass

    @abstractmethod
    def save_ballot(self, ballot: Ballot):
        pass
