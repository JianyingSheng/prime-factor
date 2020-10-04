# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import pytest
from prime import generate_prime_factors

def test_data_type():
    with pytest.raises(ValueError):
        generate_prime_factors(0.3)
