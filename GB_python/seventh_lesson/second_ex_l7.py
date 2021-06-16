from abc import ABC, abstractmethod


class Clothes:
    @abstractmethod
    def size_method(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def size_method(self):
        return round(self.v / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def size_method(self):
        return round((2 * self.h + 0.3) / 100, 2)


first_ex = Coat(54)
print(first_ex.size_method)
second_ex = Suit(180)
print(second_ex.size_method)
