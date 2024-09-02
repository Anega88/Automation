from abc import ABC, abstractmethod

class Addressable(ABC):

    @abstractmethod
    def whichAdress(self):
        pass
