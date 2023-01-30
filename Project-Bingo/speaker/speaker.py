from abc import ABC, abstractmethod


class Speaker(ABC):
    """
    Abstract class
    """

    @abstractmethod
    def speak(self, message: str):
        """
        Method used to the output audio
        """
        pass
