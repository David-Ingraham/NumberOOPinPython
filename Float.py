from Number import Number

######################################################################
class Float(Number):
    __slots__ = ("_digits")

    def __init__(self, value: float or int, digits: int = 2) -> None:
        ''' initializer method for Float class
        Parameter:
            value: a float or integer
            digits: an integer representing # of digits beyond
                decimal to be displayed when printing
        Raises:
            ValueError if value cannot be converted to float
        '''
        super().__init__(float(value))
        self._digits = digits

        

    def __add__(self, other: Number or int or float) -> Number:
        from Integer import Integer
        # you are likely to need Integer in here, so do a local-to-method
        # import (rather than global at the top) to avoid circular imports
        # (see Integer.py for an example importing Float locally)
        if isinstance(other, Float):
            return Float(self._value + other._value)
        if isinstance(other, float):
            return Float(self._value + other)
        if isinstance(other, int):
            return Integer(self._value + other)
        return Integer(self._value + other._value)
        

    def __mul__(self, other: Number or int or float) -> Number:
        # you are likely to need Integer in here, so do a local-to-method
        # import (rather than global at the top) to avoid circular imports
        # (see Integer.py for an example importing Float locally)
        from Integer import Integer

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Integer, Float, int, float])

        if isinstance(other, Float):
            return Float(self._value * other._value)
        if isinstance(other, float):
            return Float(self._value * other)
        if isinstance(other, int):
            return Integer(self._value * other)
        return Integer(self._value * other._value)

    def changeFormat(self, digits: int) -> None:
        ''' for this object, sets the number of digits to appear after the
            decimal when printed
        Parameters:
            digits: integer number of digits to appear after the decimal
        Raises:
            ValueError if digits cannot be converted to int
        '''
        self._digits = int(digits)

    def __str__(self) -> str:
        return f"{self._value:.{self._digits}f}"
