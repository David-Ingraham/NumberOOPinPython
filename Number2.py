from abc import ABC, abstractmethod

class Number(ABC): #an abstract class
    __slots__ = ("_value")



    def __init__(self, value: int or float) -> None:
        self._value = value

    @abstractmethod
    def __add__(sefl, other: 'Number') -> 'Number':
        pass

    @abstractmethod
    def __mul__(sefl, other: 'Number') -> 'Number':
        pass


    def __str__(self):
        return f"{self._value}"