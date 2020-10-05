"""
prime.py -- Write the application code here
"""

def generate_prime_factors(number_input):
    """
    function
    """
    prime_factors = []
    if not isinstance(number_input,int):
        raise ValueError

    if number_input > 1:
        i = 2
        while i * i <= number_input:
            if number_input % i == 0:
                number_input //= i
                prime_factors.append(i)
            else:
                i += 1
        if number_input > 1:
            prime_factors.append(number_input)

        if prime_factors == []:
            prime_factors.append(number_input)
    return prime_factors
