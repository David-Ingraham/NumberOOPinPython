from Number import Number

######################################################################
class Integer(Number):
    def __init__(self, value: int) -> None:
        ''' initializer method for Integer class
        Parameter:
            value: an integer
        Raises:
            ValueError if value cannot be converted to int
        '''
        super().__init__(int(value))

    def __add__(self, other: Number or int or float) -> Number:
        ''' method to add an Integer object with any object of type
            Integer, Float, int, or float
        Parameters:
            other: an Integer, Float, int, or float object
        Returns:
            a Float object if other is of type Float or float, or
            an Integer object otherwise
        Raises:
            TypeError if the type of other is not one of Integer, Float,
                int, or float
        '''
        # import Float only when needed to avoid circular import
        # (see https://bit.ly/488rlWX)
        from Float import Float

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Integer, Float, int, float])

        if isinstance(other, Float):
            return Float(self._value + other._value)
        if isinstance(other, float):
            return Float(self._value + other)
        if isinstance(other, int):
            return Integer(self._value + other)
        return Integer(self._value + other._value)

    def __mul__(self, other: Number) -> Number:
        ''' method to mulitply an Integer object with any object of type
            Integer, Float, int, or float
        Parameters:
            other: an Integer, Float, int, or float object
        Returns:
            a Float object if other is of type Float or float, or
            an Integer object otherwise
        Raises:
            TypeError if the type of other is not one of Integer, Float,
                int, or float
        '''
        # import Float only when needed to avoid circular import
        # (see https://bit.ly/488rlWX)
        from Float import Float

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Integer, Float, int, float])

        if isinstance(other, Float):
            return Float(self._value * other._value)
        if isinstance(other, float):
            return Float(self._value * other)
        if isinstance(other, int):
            return Integer(self._value * other)
        return Integer(self._value * other._value)


