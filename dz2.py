# задание 2
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def sum(self):
        pass

class Coat(Clothes):
    @property
    def sum(self):
        cons = round(self.size / 6.5, 2) + 0.5
        return (cons)

class Suit(Clothes):
    @property
    def sum(self):
        cons = (2 * self.size) + 0.3
        return (cons)

coat = Coat(54)
suit = Suit(176)
print(coat.sum)
print(suit.sum)
print(f'итого: {coat.sum + suit.sum}')
