"""
prime.py -- Write the application code here
"""
#number = input(" Please Enter any Number: ")
def generate_prime_factors(number_input):
    """
    function
    """
    prime_factors = []
    if not isinstance(number_input,int):
        raise ValueError
    if number_input > 1:
        prime_factors.append(number_input)
    return prime_factors
