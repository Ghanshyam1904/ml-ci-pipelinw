import pytest

# Function to the square
def square(n):
    return n**2

# Function to the cube
def cube(n):
    return n**3

# Function to the fifth power
def power(n):
    return n**5

# Testing the square function
def test_square():
    assert square(2) == 4 , "Test Failed: The square of 2 should be 4"
    assert square(3) == 9 , "Test Failed: The square of 3 should be 9"
    assert square(4) == 16 , "Test Failed: The square of 4 should be 16"

# Testing the cube function
def test_cube():
    assert cube(2) == 8 , "Test Failed: The cube of 2 should be 8"
    assert cube(3) == 27 , "Test Failed: The cube of 3 should be 27"
    assert cube(4) == 64 , "Test Failed: The cube of 4 should be 64"

# Test the fifth power function
def test_power():
    assert power(2) == 16 , "Test Failed: The power of 2 should be 16"
    assert power(3) == 27 , "Test Failed: The power of 3 should be 27"
    assert power(4) == 64 , "Test Failed: The power of 4 should be 64"

# Test for the invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square('string')