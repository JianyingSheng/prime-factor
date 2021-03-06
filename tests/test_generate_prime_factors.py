# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import pytest
from prime import generate_prime_factors

def test_data_type():
    """
    Test the type of input number, integer expected
    """
    with pytest.raises(ValueError):
        generate_prime_factors(0.3)


def test_one_prime_factors():
    """
    The prime factor of one is an empty list
    """
    assert generate_prime_factors(1) == []


def test_two_prime_factors():
    """
    The prime factor of two is 2
    """
    assert generate_prime_factors(2) == [2]


def test_three_prime_factors():
    """
    The prime factor of three is 3
    """
    assert generate_prime_factors(3) == [3]

def test_four_prime_factors():
    """
    The prime factor of four is [2,2]
    """
    assert generate_prime_factors(4) == [2,2]

def test_six_prime_factors():
    """
    The prime factor of six is [2,3]
    """
    assert generate_prime_factors(6) == [2,3]

def test_eight_prime_factors():
    """
    The prime factor of eight is [2,2,2]
    """
    assert generate_prime_factors(8) == [2,2,2]

def test_nine_prime_factors():
    """
    The prime factor of nine is [3,3]
    """
    assert generate_prime_factors(9) == [3,3]
