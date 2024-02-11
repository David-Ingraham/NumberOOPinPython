from abc import ABC, abstractmethod #no native abstrac classes in python 



class Parent(ABC):
    def __init__(self, value:int)-> None:
        self._value = value

    @abstractmethod #you can not instanstiate a object if it inherits this method
    def commonMethod(self):
        print(f'{self._value}')

    def __str__(self):
        print( f"{self.__name__}: {self._value}")


class Child(Parent):

    def __init__(self,value, name)-> None:

        super().__init__(value)

        self._name = name


    def commonMethod(self):
        print(f"{self._name}: {self._value}")


def main()->None:

    p = Parent(39)
    p.commonMethod()

    c = Child(39,"kid")

    c.commonMethod()



if __name__ == '__name__':
    main()