from Number import Number

class Complex(Number):
    def __init__(self, value: float, imaginary: float, precision: int = 2) -> None:
        super().__init__(value)
        self._imaginary = imaginary
        self._precision = precision

    def __str__(self) -> str:
        # Format real and imaginary parts with specified precision
        value_formatted = f"{self._value:.{self._precision}f}".rstrip('0').rstrip('.')
        imaginary_formatted = f"{abs(self._imaginary):.{self._precision}f}".rstrip('0').rstrip('.')

        # Handle case of zero for both value (real) and imaginary parts
        if self._value == 0 and self._imaginary == 0:
            return "0"
        # Handle value (real) part only
        elif self._imaginary == 0:
            return value_formatted
        # Handle imaginary part only
        elif self._value == 0:
            return f"{self._imaginary:+g}i" if self._imaginary != 1 and self._imaginary != -1 else f"{'-' if self._imaginary == -1 else ''}i"
        # Handle both value (real) and imaginary parts
        else:
            sign = "+" if self._imaginary > 0 else "-"
            imaginary_part = f"{imaginary_formatted}i" if abs(self._imaginary) != 1 else "i"
            return f"{value_formatted} {sign} {imaginary_part}" if abs(self._imaginary) != 1 else f"{value_formatted} {sign}{imaginary_part}"
        

    def __add__(self, other):

        real = f'{(self._value + other._value):.{self._precision}f}'
        compelx = f'{(self._imaginary + other._imaginary):.{self._precision}f}'

        #return f'{real} + {compelx}i'

        real = float(real)
        compelx = float(compelx)

        return Complex(real,compelx, self._precision)
    
    def __mul__(self, other):

        real = float(f'{(self._value * other._value):.{self._precision}f}')
        compelx = float(f'{(self._imaginary * other._imaginary):.{self._precision}f}')

        return Complex(real, compelx)






a = Complex(1.23456, 2.34567, precision=3)
b = Complex(1,4)
c= Complex(3,4)
print(a)  # Example with precision set to 3
print(a*c)
print(a+c)