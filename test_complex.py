from Complex import Complex
import random
import pytest

from test_Float import random_float 

# Fixtures for generating random complex numbers
@pytest.fixture
def random_complex() -> Complex:
    real = random.uniform(-100, 100)
    imaginary = random.uniform(-100, 100)
    return Complex(real, imaginary)

@pytest.fixture
def random_complex_with_precision() -> Complex:
    real = random.uniform(-100, 100)
    imaginary = random.uniform(-100, 100)
    precision = random.choice([0, 2, 4])
    return Complex(real, imaginary, precision)

@pytest.fixture
def zero_complex() -> Complex:
    return Complex(0, 0)

#@pytest.fixture
#def zero_real(random) ->
 #   return Complex()

# Test initialization and string representation
def test_Complex_init_and_str(random_complex_with_precision):
    complex_str = str(random_complex_with_precision)
    real = random_complex_with_precision._value
    imaginary = random_complex_with_precision._imaginary
    precision = random_complex_with_precision._precision
    assert isinstance(random_complex_with_precision, Complex)
    assert f"{real:.{precision}f}" in complex_str
    assert f"{imaginary:.{precision}f}" in complex_str or "i" in complex_str

# Test addition of two Complex objects
def test_add_two_Complex_objects(random_complex, random_complex_with_precision):
    result = random_complex + random_complex_with_precision
    expected_real = random_complex._value + random_complex_with_precision._value
    expected_imaginary = random_complex._imaginary + random_complex_with_precision._imaginary
    
    assert isinstance(result, Complex)
    
    # Check if real parts are approximately equal
    assert abs(result._value - expected_real) <= 0.01
    
    # Manually check if imaginary parts are approximately equal within the tolerance
    assert abs(result._imaginary - expected_imaginary) <= 0.01, \
        f"Imaginary parts differ: {result._imaginary} != {expected_imaginary} within tolerance"


# Test multiplication of two Complex objects
def test_multiply_two_Complex_objects(random_complex, random_complex_with_precision):
    result = random_complex * random_complex_with_precision
    # For simplicity, this example does not perform the actual complex multiplication formula
    # You can expand this to accurately test complex multiplication
    assert isinstance(result, Complex)

# Test Complex object with zero
def test_add_Complex_to_zero(random_complex, zero_complex):
    result = random_complex + zero_complex
    assert isinstance(result, Complex)
    assert round(result._value) == round(random_complex._value)
    assert round(result._imaginary) == round(random_complex._imaginary)

# Test Complex object multiplication by zero
def test_multiply_Complex_by_zero(random_complex, zero_complex):
    result = random_complex * zero_complex
    assert isinstance(result, Complex)
    assert result._value == 0
    assert result._imaginary == 0

# Additional tests for string representation, changing precision, etc., can be added following the pattern above.

