

class Number:
    __slots__ = ('_value',)

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Value must be int or float')
        
        if value < 0:
            raise ValueError('Value must be positive')

        self._value = value

    def __str__(self):
        return f'{self._value}'

    def __add__(self, other):
        if not isinstance(other, Number) or isinstance(other, Integer) or isinstance(other, Float):
            raise TypeError('Value must be Number')
        
        if isinstance(self._value, int) and isinstance(other._value, int):
            return Integer(self._value + other._value)
        
        else:
            return Float(self._value + other._value)

        
        

    def __mul__(self, other):
        if not isinstance(other, Number):
            raise TypeError('Value must be Number')
        if isinstance(self._value, int) and isinstance(other._value, int):
            return Integer(self._value * other._value)
        
        else:
            return Float(self._value * other._value)
    


class Integer(Number):
    

    def __init__(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError('Value must be int')
        if value < 0:
            raise ValueError('Value must be positive')
        super().__init__(value)

class Float(Number):
    __slots__ = ("_digits_to_precisiosn")


    def __init__(self, value: float, digits_to_precisiosn: int = 2) -> None:
        super().__init__(value)
        self._digits_to_precisiosn = digits_to_precisiosn
        self._value = value

        if not isinstance(digits_to_precisiosn, int):
            raise TypeError('digits_to_precisiosn must be int')
        if digits_to_precisiosn < 0:
            raise ValueError('digits_to_precisiosn must be positive')
        if not isinstance(value, float):
            raise TypeError('Value must be float')

   
    def changeFormat(self, new_precesicion)-> None: #setter method, changes value of self.digits_to_precisiosn to argument passed in for new_precesicion parameter
        if not isinstance(new_precesicion, int):
            raise TypeError('new_precesicion must be int')
        if new_precesicion < 0:
            raise ValueError('new_precesicion must be positive')
        self._digits_to_precisiosn = new_precesicion


    def __str__(self)-> str:
        return f"{self._value:.{self._digits_to_precisiosn}f}"
    

#s= f"{num:.{digits_to_precisiosn}f}"


#order matters for mull and add methods when you invoke them
    # if i do a * b and a is my cutstom integer class while b is the built in int, b would be the 'other' argument and i could handdle
    #the type of other in my method defintion. b * a tho will not work becuase the mull method in the built in int class is not code that im writting
    #so it may not be able to handle it
    
    
def main():
    a = Number(10.5)
    b = Number(20)

    print(f'testing a + b \n{a + b}\n')
    print(f'testing a * b \n{a * b}\n')

    c = Integer(10)
    d = Integer(20)

    print(f'testing c + d \n{c + d}\n')
    print(f'testing c * d \n{c * d}\n')


    e = Float(10.59086, 2)
    f = Float(20.92728, 2)

    print(f'testing e + f \n{e + f}\n')

    print(f'testing e * f \n{e * f}\n')

    g = Integer(10)
    h = Float(10.1,2)

    print(f'testing 10 * 10.1 \n{g * h}\n')

    print(f'testing changeFormat Method. The numbber was {e} and was originally fromated to {e._digits_to_precisiosn} points of precicison')
    e.changeFormat(4)

    print(f'Points to precision is now : {e._digits_to_precisiosn}')

    print(e)

    print(f'testing adding built in int class to custom Integer class \n{d + 10}\n')

    #line 119 throws an error, __add__ method is checking for input to be Number object
    

if __name__ == '__main__':
    main()





# Output:
# testing a + b 
# 30

# testing a * b 
# 200