from Float import Float
from Integer import Integer
import random

import pytest


@pytest.fixture
def random_float():
    x = 0
    l = []

    for i in range(1,1000):
        l.append((i*0.99) + x)
        x = x + 1

    return l[random.randint(1, len(l)-1)]


@pytest.fixture
def random_Float_two_decimals(random_float):
    return Float(random_float)


@pytest.fixture
def zero_Float_str_two_decimals():
    return Float(0)


@pytest.fixture
def zero_Float_str_four_decimals():
    return Float(0,4)


@pytest.fixture
def random_Float_two_decimals(random_float):
    return Float(random_float)


@pytest.fixture
def random_Float_four_decimals(random_float):
    return Float(random_float, 4)


@pytest.fixture
def random_Float_zero_decimals(random_float):
    return Float(random_float, 0)






######################################################################
def test_Float_init() -> None:
    ''' given: a float
        when:  an Float object is created using that float
        then:  an object of type Float, with appropriate _value 
               should be created
    '''
    value = random.random() * 1000
    f = Float(value)
    assert(isinstance(f, Float))
    assert(f._value == value)

######################################################################

def test_zero_Float_str_two_decimals() -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default two decimals
    '''
    i = Float(0)
    assert(i.__str__() == "0.00")

def test_zero_Float_str_four_decimals() -> None:
    ''' given: a Float object with zero value
        when:  that object is printed
        then:  __str__ should return an appropriate string
                with default four decimals
    '''
    i = Float(0, 4)
    assert(i.__str__() == "0.0000")

def test_positive_Float_str_two_decimals() -> None:
    ''' given: a Float object with positive value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    value = random.random() * 100
    f = Float(value)
    assert(f.__str__() == f"{value:.2f}")

def test_positive_Float_str_four_decimals() -> None:
    ''' given: a Float object with positive value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    value = random.random() * 100
    f = Float(value, 4)
    assert(f.__str__() == f"{value:.4f}")

def test_positive_Float_str_zero_decimals() -> None:
    ''' given: a Float object with positive value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    value = random.random() * 100
    f = Float(value, 0)
    assert(f.__str__() == f"{value:.0f}")

def test_negative_Float_str_two_decimals() -> None:
    ''' given: a Float object with negative value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    value = -random.random() * 100
    f = Float(value)
    assert(f.__str__() == f"{value:.2f}")

def test_negative_Float_str_four_decimals() -> None:
    ''' given: a Float object with negative value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    value = -random.random() * 100
    f = Float(value, 4)
    assert(f.__str__() == f"{value:.4f}")

def test_negative_Float_str_zero_decimals() -> None:
    ''' given: a Float object with negative value
        when:  that object is printed
        then:  __str__ should return an appropriate string with default two
            decimals
    '''
    value = -random.random() * 100
    f = Float(value, 0)
    assert(f.__str__() == f"{value:.0f}")

######################################################################

def test_changeFormat_zero_decimals() -> None:
    ''' given: a Float object with default two decimals
        when:  changeFormat is called indicating zero decimals
        then:  __str__ should return an appropriate string with zero
            decimals
    '''
    value = random.random() * 100
    f = Float(value)
    assert(f.__str__() == f"{value:.2f}")
    f.changeFormat(0)
    assert(f.__str__() == f"{value:.0f}")

def test_changeFormat_four_decimals() -> None:
    ''' given: a Float object with default two decimals
        when:  changeFormat is called indicating four decimals
        then:  __str__ should return an appropriate string with four
            decimals
    '''
    value = random.random() * 100
    f = Float(value)
    assert(f.__str__() == f"{value:.2f}")
    f.changeFormat(4)
    assert(f.__str__() == f"{value:.4f}")

######################################################################

# your pytest functions for __add__ and __mul__ go below..."""
