from Integer import Integer
from Float import Float
import pytest
import random

######################################################################


@pytest.fixture
def random_integer()-> int:
    return random.randint(1,1000)

@pytest.fixture
def random_Integer(random_integer: int)-> Integer:
    return Integer(random_integer)

@pytest.fixture 
def zero_Integer_str() -> Integer:
       
    return Integer(0)

@pytest.fixture
def random_negative_int()->int:
    return random.randint(-1000,-1)

@pytest.fixture
def random_negative_Integer(random_negative_int: int)-> Integer:
    return Integer(random_negative_int)

@pytest.fixture
def random_float() -> float:
    """Fixture to generate a random float value."""
    return random.uniform(-1000, 1000)

@pytest.fixture
def random_Float(random_float: float) -> Float:
    """Fixture to create a Float object with a random float value."""
    return Float(random_float)

@pytest.fixture
def two_random_Integers() -> 'tuple[Integer, Integer]':
    """Fixture to generate a tuple of two random Integer objects."""
    return (Integer(random.randint(1, 1000)), Integer(random.randint(1, 1000)))

@pytest.fixture
def integer_and_int() -> 'tuple[Integer, int]':
    """Fixture to generate an Integer object and a random int."""
    return (Integer(random.randint(1, 1000)), random.randint(1, 1000))

@pytest.fixture
def integer_and_float() -> 'tuple[Integer, float]':
    """Fixture to generate an Integer object and a random float."""
    return (Integer(random.randint(1, 1000)), random.uniform(-1000, 1000))

@pytest.fixture
def integer_and_Float() -> 'tuple[Integer, Float]':
    """Fixture to generate an Integer object and a Float object."""
    return (Integer(random.randint(1, 1000)), Float(random.uniform(-1000, 1000)))




    


def test_Integer_init(random_integer, random_Integer) -> None: #pytest fixtures photo in iphone camera role 
    ''' given: an int
        when:  an Integer object is created using that int
        then:  an object of type Integer, with appropriate _value 
               should be created
    '''

    assert(isinstance(random_Integer, Integer))
    assert(random_Integer._value == random_integer)

######################################################################

def test_zero_Integer_str(zero_Integer_str) -> None:
    ''' given: an Integer object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
    '''


    #i = Integer(0)
    assert(zero_Integer_str.__str__() == "0")

def test_positive_Integer_str(random_Integer) -> None:
    ''' given: an Integer object with positive value
        when:  that object is printed
        then:  __str__ should return an appropriate string
    '''
    #value = random.randint(1,1000)
    #i = Integer(value)
    assert(random_Integer.__str__() == str(random_Integer._value))

def test_negative_Integer_str(random_negative_Integer) -> None:
    ''' given: an Integer object with negative value
        when:  that object is printed
        then:  __str__ should return an appropriate string
    '''
    #value = -random.randint(1,1000)
    #i = Integer(value)
    assert(random_negative_Integer.__str__() == str(random_negative_Integer._value))

######################################################################
# Using the two_random_Integers fixture
def test_add_Integer_and_Integer(two_random_Integers) -> None:
    i1, i2 = two_random_Integers
    i3 = i1 + i2
    assert isinstance(i3, Integer)
    assert i3._value == i1._value + i2._value

# Using the integer_and_int fixture
def test_add_Integer_and_int(integer_and_int) -> None:
    i1, i2 = integer_and_int
    i3 = i1 + i2
    assert isinstance(i3, Integer)
    assert i3._value == i1._value + i2

# Using the integer_and_float fixture
def test_add_Integer_and_float(integer_and_float) -> None:
    i1, f1 = integer_and_float
    f2 = i1 + f1
    assert isinstance(f2, Float)
    assert abs(f2._value - (i1._value + f1)) < 1e-6

# Using the integer_and_Float fixture
def test_add_Integer_and_Float(integer_and_Float) -> None:
    i1, f1 = integer_and_Float
    f2 = i1 + f1
    assert isinstance(f2, Float)
    assert abs(f2._value - (i1._value + f1._value)) < 1e-6

# For multiplication tests, we can use the same approach:

# Using the two_random_Integers fixture
def test_multiply_Integer_and_Integer(two_random_Integers) -> None:
    i1, i2 = two_random_Integers
    i3 = i1 * i2
    assert isinstance(i3, Integer)
    assert i3._value == i1._value * i2._value

# Using the integer_and_int fixture
def test_multiply_Integer_and_int(integer_and_int) -> None:
    i1, i2 = integer_and_int
    i3 = i1 * i2
    assert isinstance(i3, Integer)
    assert i3._value == i1._value * i2

# Using the integer_and_float fixture
def test_multiply_Integer_and_float(integer_and_float) -> None:
    i1, f1 = integer_and_float
    f2 = i1 * f1
    assert isinstance(f2, Float)
    assert abs(f2._value - (i1._value * f1)) < 1e-6

# Using the integer_and_Float fixture
def test_multiply_Integer_and_Float(integer_and_Float) -> None:
    i1, f1 = integer_and_Float
    f2 = i1 * f1
    assert isinstance(f2, Float)
    assert abs(f2._value - (i1._value * f1._value)) < 1e-6

