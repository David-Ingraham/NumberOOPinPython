from Float import Float
from Integer import Integer
import random

import pytest


@pytest.fixture
def random_float()->float:
    x = 0
    l = []

    for i in range(1,1000):
        l.append((i*0.99) + x)
        x = x + 1

    return l[random.randint(1, len(l)-1)]

@pytest.fixture
def random_negative_float()-> float:

    x= -999
    l = []

    for i in range(-1000, -1):
        l.append((i*0.99) + x)
        x = x + 1

    return l[random.randint(1,len(l)-1)]


@pytest.fixture
def random_Float_two_decimals(random_float: float) -> Float:
    return Float(random_float)


@pytest.fixture
def zero_Float_str_two_decimals()-> Float:
    return Float(0)


@pytest.fixture
def zero_Float_str_four_decimals()-> Float:
    return Float(0,4)


@pytest.fixture
def random_Float_two_decimals(random_float)-> Float:
    return Float(random_float)


@pytest.fixture
def random_Float_four_decimals(random_float)-> Float:
    return Float(random_float, 4)


@pytest.fixture
def random_Float_zero_decimals(random_float)-> Float:
    return Float(random_float, 0)

@pytest.fixture
def random_negative_Float_two_decimals(random_negative_float)-> Float:
    return Float(random_negative_float)



@pytest.fixture
def random_negative_Float_four_decimals(random_negative_float)-> Float:
    return Float(random_negative_float, 4)



@pytest.fixture
def random_negative_Float_zero_decimals(random_negative_float)-> Float:
    return Float(random_negative_float, 0)



######################################################################
def test_Float_init(random_float, random_Float_two_decimals) -> None:
    ''' given: a float
        when:  an Float object is created using that float
        then:  an object of type Float, with appropriate _value 
               should be created
    '''
    #value = random.random() * 1000
    #f = Float(value)


    assert(isinstance(random_Float_two_decimals, Float))
    assert(random_Float_two_decimals._value == random_float)

######################################################################

def test_zero_Float_str_two_decimals(zero_Float_str_two_decimals) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    #i = Float(0)
    assert(zero_Float_str_two_decimals.__str__() == "0.00")

def test_zero_Float_str_four_decimals(zero_Float_str_four_decimals) -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default four decimals
    '''
    #i = Float(0, 4)
    assert(zero_Float_str_four_decimals.__str__() == "0.0000")

def test_positive_Float_str_two_decimals(random_Float_two_decimals) -> None:
    ''' given: a Float object with positive value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    #value = random.random() * 100
    #f = Float(value)
    assert(random_Float_two_decimals.__str__() == f"{random_Float_two_decimals._value:.2f}")

def test_positive_Float_str_four_decimals(random_Float_four_decimals) -> None:
    ''' given: a Float object with positive value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    #value = random.random() * 100
    #f = Float(value, 4)
    assert(random_Float_four_decimals.__str__() == f"{random_Float_four_decimals._value:.4f}")

def test_positive_Float_str_zero_decimals(random_Float_zero_decimals) -> None:
    ''' given: a Float object with positive value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    #value = random.random() * 100
    #f = Float(value, 0)
    assert(random_Float_zero_decimals.__str__() == f"{random_Float_zero_decimals._value:.0f}")

def test_negative_Float_str_two_decimals(random_negative_Float_two_decimals) -> None:
    ''' given: a Float object with negative value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    #value = -random.random() * 100
    #f = Float(value)
    assert(random_negative_Float_two_decimals.__str__() == f"{random_negative_Float_two_decimals._value:.2f}")

def test_negative_Float_str_four_decimals(random_negative_Float_four_decimals) -> None:
    ''' given: a Float object with negative value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    #value = -random.random() * 100
    #f = Float(value, 4)
    assert(random_negative_Float_four_decimals.__str__() == f"{random_negative_Float_four_decimals._value:.4f}")

def test_negative_Float_str_zero_decimals(random_negative_Float_zero_decimals) -> None:
    ''' given: a Float object with negative value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    #value = -random.random() * 100
    #f = Float(value, 0)
    assert(random_negative_Float_zero_decimals.__str__() == f"{random_negative_Float_zero_decimals._value:.0f}")

######################################################################

def test_changeFormat_zero_decimals(random_Float_two_decimals) -> None:
    ''' given: a Float object with default two decimals
        when:  changeFormat is called indicating zero decimals
        then:  __str__ should return an appropriate string with zero
            decimals
    '''
    ##\value = random.random() * 100
    #f = Float(value)
    assert(random_Float_two_decimals.__str__() == f"{random_Float_two_decimals._value:.2f}")
    random_Float_two_decimals.changeFormat(0)
    assert(random_Float_two_decimals.__str__() == f"{random_Float_two_decimals._value:.0f}")

def test_changeFormat_four_decimals(random_Float_two_decimals) -> None:
    ''' given: a Float object with default two decimals
        when:  changeFormat is called indicating four decimals
        then:  __str__ should return an appropriate string with four
            decimals
    '''
    #value = random.random() * 100
    #f = Float(value)
    assert(random_Float_two_decimals.__str__() == f"{random_Float_two_decimals._value:.2f}")
    random_Float_two_decimals.changeFormat(4)
    assert(random_Float_two_decimals.__str__() == f"{random_Float_two_decimals._value:.4f}")

######################################################################

# your pytest functions for __add__ and __mul__ go below..."""


# Test adding two random Float objects with two decimals
def test_add_two_random_Float_objects(random_Float_two_decimals, random_Float_four_decimals):
    expected_value = random_Float_two_decimals._value + random_Float_four_decimals._value
    result = random_Float_two_decimals + random_Float_four_decimals
    assert isinstance(result, Float), "Result of addition should be a Float object"
    assert result._value == pytest.approx(expected_value), "The sum does not match the expected value"

# Test multiplying a random and a negative Float object
def test_multiply_random_and_negative_Float(random_Float_two_decimals, random_negative_Float_two_decimals):
    expected_value = random_Float_two_decimals._value * random_negative_Float_two_decimals._value
    result = random_Float_two_decimals * random_negative_Float_two_decimals
    assert isinstance(result, Float), "Result of multiplication should be a Float object"
    assert result._value == pytest.approx(expected_value), "The product does not match the expected value"

# Test adding a random Float to a zero Float
def test_add_random_Float_to_zero(random_Float_two_decimals, zero_Float_str_two_decimals):
    result = random_Float_two_decimals + zero_Float_str_two_decimals
    assert isinstance(result, Float), "Result of addition should be a Float object"
    assert result._value == pytest.approx(random_Float_two_decimals._value), "Adding zero should not change the value"

# Test multiplying a random Float by a zero Float
def test_multiply_random_Float_by_zero(random_Float_two_decimals, zero_Float_str_two_decimals):
    result = random_Float_two_decimals * zero_Float_str_two_decimals
    assert isinstance(result, Float), "Result of multiplication should be a Float object"
    assert result._value == 0, "Multiplying by zero should result in zero"

# Test string representation of a random Float with four decimals
def test_str_random_Float_four_decimals(random_Float_four_decimals):
    expected_str = f"{random_Float_four_decimals._value:.4f}"
    assert str(random_Float_four_decimals) == expected_str, "String representation does not match expected format"

# Test adding two negative Float objects
def test_add_two_negative_Float_objects(random_negative_Float_two_decimals, random_negative_Float_four_decimals):
    expected_value = random_negative_Float_two_decimals._value + random_negative_Float_four_decimals._value
    result = random_negative_Float_two_decimals + random_negative_Float_four_decimals
    assert isinstance(result, Float), "Result of addition should be a Float object"
    assert result._value == pytest.approx(expected_value), "The sum of negative values does not match the expected value"

# Test changing format of a Float object after addition
def test_changeFormat_after_addition(random_Float_two_decimals, random_Float_four_decimals):
    result = random_Float_two_decimals + random_Float_four_decimals
    result.changeFormat(0)  # Changing to zero decimals
    expected_str = f"{result._value:.0f}"
    assert str(result) == expected_str, "String representation after format change does not match expected"
